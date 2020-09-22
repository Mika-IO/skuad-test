# coding: utf-8
import requests
import sys
from tqdm import tqdm
from script1 import templating, flow_definer, require_data 
from pathlib import Path
import csv


def read_data(directory, period):
    '''
        Realiza a leitura do arquivo no caminho escolhido
    '''
    file_name = templating(period)[1]
    if  True:
        path = Path(f'{directory}/{file_name}')
        print(file_name)
        if path.is_file():
            path = f'{directory}/{file_name}'
            with open(path, 'rb') as file:
                reader = csv.DictReader(file, delimiter=',')  
                print(reader)
                for column in tqdm(reader, desc=f'Analizando {file_name}'):
                    print(column)
            print('\n')
        else:
            print('\nArquivo não econtrado')
    else:
        print('\nAlgo deu errado!!')

if __name__ == "__main__":
    flow_definer(sys.argv, read_data)
