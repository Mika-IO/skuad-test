# coding: utf-8
import requests
import os
import sys
from tqdm import tqdm


def templating_url(period):
    '''
        Retorna o nome do Arquivo CSV e a url do arquivo
    '''
    name = f'inf_diario_fi_{period}.csv'
    url = f'http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/{name}'
    return url, name


def require_data():
    '''
        Retorna as entradas do usuário, os paramêtros (directory, period)
    '''
    print('########## Entre com os parâmetros ##########')
    directory = input('\nDigite o caminho onde será salvo o CSV: ')
    period = input('\nDigite o período do arquivo CSV no formato YYYYMM: ')
    return directory, period


def stream_data(directory, period):
    '''
        Realiza o download e salva o arquivo no caminho escolhido
    '''
    url, file_name = templating_url(period)
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


def main(parameters):
    '''
        Fluxo principal
        Define o fluxo de acordo com os paramêtros passados para o script
    '''
    if not parameters[1:]:
        directory, period = require_data()
        stream_data(directory, period)
    else:
        directory = str(parameters[1])
        period = str(parameters[2])
        stream_data(directory, period)


if __name__ == "__main__":
    main(sys.argv)
