from fastapi import FastAPI
import os
from random import randint
import pandas as pd
from tqdm import tqdm
from script1 import stream_data
from script2 import quota_price_variation
from script2 import trunc

'''
    period 202003
    cnpjs 00.017.024_0001-53,00.071.477_0001-68,00.102.322_0001-41
'''


def json_relatory_generator(period: int, args: list) -> dict :
    '''
        Gera um relatório dos cnpjs de determinado período com
            variação do preço da cota
            captação mensal do fundo
            resgate mensal do fundo
    '''  
    id = randint(0, 1000)
    stream_data('.', period, id)
    with open(f'{id} -- inf_diario_fi_{period}.csv') as file:
        file_name = f'{id} -- inf_diario_fi_{period}.csv'
    directory = '.'
    if True:
        path = f'{directory}/{file_name}'
        with open(path, 'r') as file:
            print('Analizando arquivos...')
            file = pd.read_csv(file_name, sep=';')
            file = file.filter(items=[
                'CNPJ_FUNDO',
                'VL_QUOTA',
                'CAPTC_DIA',
                'RESG_DIA'
                ])
            variation_array = []
            captured_array = []
            rescue_array = []
            for arg in args:
                fund = file.loc[file['CNPJ_FUNDO'] == arg]
                # Price variation
                first_position = list(fund.index)[0]
                last_position = list(fund.index)[-1]
                first_position = fund['VL_QUOTA'][first_position]
                last_position = fund['VL_QUOTA'][last_position]
                variation = quota_price_variation(
                    float(first_position),
                    float(last_position)
                    )
                # Captured
                index = list(fund.index)
                captured = 0
                for i in index:
                    captured += fund['CAPTC_DIA'][i]
                # Rescue
                rescue = 0
                for i in index:
                    rescue += fund['CAPTC_DIA'][i]
                variation_array.append(trunc(variation, 2))
                captured_array.append(trunc(captured, 2))
                rescue_array.append(trunc(rescue, 2))
            data_result = {
                'cnpj': args,
                'price_variation_percent': variation_array,
                'month_capturation': captured_array,
                'month_rescue': rescue_array,
            }
            os.remove(f'{id} -- inf_diario_fi_{period}.csv')
            return data_result
    else:
        return {'mensagem' : 'algo deu errado'}
        

app = FastAPI()


@app.post("/relatory/{period}/{cnpjs}")
def fi_relatory(period: int, cnpjs: str):
    '''
        Rota de relatório de FI
        
        Parametros:
        
        Periodo YYYYMM
        
        CNPJs dividos por vírgula
        
        Exemplo:  

        Período = 202005

        CNPJS = 00.017.024_0001-53,00.071.477_0001-68,00.102.322_0001-41

        OBS: / deve ser substituido por _ nos CNPJs
    '''
    cnpjs = cnpjs.replace('_', '/')
    cnpjs = cnpjs.split(',')
    if len(str(period)) != 6:
        return {"error": "Paramêtros inválidos"}
    for cnpj in cnpjs:
        if len(cnpj) != 18:
            return {"error": "Paramêtros inválidos"}
    else:
        return json_relatory_generator(period, cnpjs)
