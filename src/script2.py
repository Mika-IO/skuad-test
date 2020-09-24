# coding: utf-8
import sys
from tqdm import tqdm
from script1 import templating
from pathlib import Path
import pandas as pd
import csv
import math
import json
from time import sleep


def trunc(number, digits=4) -> float:
    '''
        Reduz as casas decimais de um float apôs o ponto
    '''
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


def all_cnpjs(file):
    '''
        Retorna todos os cnpjs do arquivo
    '''
    file = file.filter(items=['CNPJ_FUNDO'])
    file = file.drop_duplicates()
    file = file.values
    result = []
    for f in file:
        result.append(f[0])
    return result


def quota_price_variation(first_month_price, last_month_price) -> float:
    '''
        Calcula a variação de preço da cota
    '''
    first_month_price = trunc(first_month_price, 4)
    last_month_price = trunc(last_month_price, 4)
    try:
        return (last_month_price/first_month_price - 1) * 100
    except (RuntimeError, ZeroDivisionError):
        return 0


def analize_data(directory, period, *args) -> dict:
    '''
        Realiza a analize do arquivo no caminho escolhido
    '''
    file_name = templating(period)[1]
    if True:
        path = Path(f'{directory}/{file_name}')
        if path.is_file():
            path = f'{directory}/{file_name}'
            with open(path, 'r') as file:
                file = pd.read_csv(file_name, sep=';')
                file = file.filter(items=[
                    'CNPJ_FUNDO',
                    'VL_QUOTA',
                    'CAPTC_DIA',
                    'RESG_DIA'
                    ])
                check = True if (len(args[0])) == 0 else False
                if check: 
                    print('\nAnalizar o arquivo todo pode demorar...')
                    print('Use o filtro de CNPJ...\n')
                args = all_cnpjs(file) if (len(args[0])) == 0 else args[0]
                variation_array = []
                captured_array = []
                rescue_array = []
                progress_bar = tqdm(total=int(len(args)), desc=f'Analizando CSV')
                for arg in args:
                    progress_bar.update(1)
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
                return data_result
        else:
            print('\nArquivo não econtrado')
    else:
        print('\nAlgo deu errado!!')


def make_html(directory, period, dict_relatory):
    '''
        Cria uma página html com a análise dos arquivos
    '''
    def make_line(cnpj, variation, captation, rescue):
        container_template = f'''
            <tr>
                <td>{cnpj}</td>
                <td>{variation}</td>
                <td>{captation}</td>
                <td>{rescue}</td>
            </tr>
        '''
        return container_template

    container = f''
    for i in range(len(dict_relatory['cnpj'])):
        container += make_line(
            dict_relatory['cnpj'][i],
            dict_relatory['price_variation_percent'][i],
            dict_relatory['month_capturation'][i],
            dict_relatory['month_rescue'][i],
        )
    page = f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Relatório</title>
        </head>
        <body>
            <style>
            </style>
            <h1 align="center">Relatório dos fundos imobiliários</h1>
            <table border='1' align="center">
                <tr>
                    <th>CNPJ</td>
                    <th>Variação mensal do preço da cota %</th>
                    <th>Captação mensal do fundo</th>
                    <th>Resgate mensal do fundo</th>
                </tr>
                {container}
            </table>
        </body>
        </html>
    '''
    with open(f'{directory}/Relatório{period}.html', 'w') as file:
        file.write(page)
    print('\nRelatório gerado com sucesso\n')


def flow_definer(parameters):
    '''
        Define o fluxo de acordo com os valores passados por parametro
    '''
    if not parameters[2:] or parameters[1] == '-help':
        print('\n-- help --\n')
        print('\nDIGITE OS PARAMÊTROS PARA O SCRIPT\n')
        print('diretório - /directory/sub_directory/')
        print('período   - YYYYMM')
        print('CNPJ(s)   - 00.000.000/0000-00')
        print('\n-- exemplo --\n')
        print('python script2.py . 00.000.000/0000-00\n')
    else:
        directory = str(parameters[1])
        period = str(parameters[2])
        args = parameters[3:]
        relatory = analize_data(directory, period, args)
        make_html(directory, period, relatory)


if __name__ == "__main__":
    flow_definer(sys.argv)
