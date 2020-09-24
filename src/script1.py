# coding: utf-8
import requests
import sys
from tqdm import tqdm


def templating(period: str ) -> tuple:
    '''
        Retorna o nome do Arquivo CSV e a url do arquivo
    '''
    name = f'inf_diario_fi_{period}.csv'
    url = f'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{name}'
    return url, name


def require_data() -> tuple:
    '''
        Retorna as entradas do usuário, os paramêtros (directory, period)
    '''
    print('\n########## Entre com os parâmetros ##########')
    directory = input('\nDigite o caminho para o arquivo CSV: ')
    period = input('\nDigite o período do arquivo CSV no formato YYYYMM: ')
    return directory, period


def stream_data(directory, period):
    '''
        Realiza o download e salva o arquivo no caminho escolhido
    '''
    url, file_name = templating(period)
    print(f'\nDownloading {file_name}\n')
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get('content-length', 0))
    block_size = 4096
    download_bar = tqdm(
        total=file_size,
        unit='iB',
        unit_scale=True,
        desc=file_name)
    try:
        with open(f'{directory}/{file_name}', 'wb') as file:
            for block in response.iter_content(chunk_size=block_size):
                download_bar.update(len(block))
                file.write(block)
        download_bar.close()
        print('\nDownload complete') if file_size != 0 else print('\nDownload error')
    except:
        print('\nAlgo deu errado!!')


def flow_definer(parameters, data_handle):
    '''
        Define o fluxo de acordo com os paramêtros passados para o script ou não
    '''
    if not parameters[1:]:
        directory, period = require_data()
        data_handle(directory, period)
    else:
        directory = str(parameters[1])
        period = str(parameters[2])
        data_handle(directory, period)


if __name__ == "__main__":
    flow_definer(sys.argv, stream_data)
