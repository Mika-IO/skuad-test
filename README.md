<div align='center'>
    <h1>Desafio</h1>
    <img src='https://img.shields.io/badge/python-3.7.3-blue'></img>
    <img src='https://img.shields.io/github/license/Mika-IO/skuak-test'></img>
    <img src='https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FMLevanto'></img>
</div>

[Link dos arquivos CSV](http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/)

[Dicionário dos Dados CSV](http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/META/meta_inf_diario_fi.txt)

## ***Exercício 1*** :hammer_and_wrench:
Escreva um script em python que faça o download de um arquivo CSV, e salve em um diretório local. 

O script deverá receber **dois parâmetros**: *o diretório onde o arquivo deverá ser salvo, e um mês específico no formato YYYYMM.*

## ***Exercício 2*** :hammer_and_wrench:
A partir dos arquivos obtidos no exercício anterior, faça um script que gere um relatório contendo:

- A porcentagem de variação do valor da cota.

- O valor captado entre o primeiro e último dia disponível de um mês específico.

- O valor resgatado de um fundo entre o primeiro e último dia disponível de um mês específico.

Este script deverá receber como parâmetros:
- O mês desejado no formato YYYYMM.
- O caminho do diretório onde estão os arquivos CSV.
- Receber uma lista de CNPJs. 

O script deverá calcular os valores para cada CNPJ se uma lista de CNPJs for passada por parâmetro. Caso nenhum CNPJ seja informado, o script deverá gerar um relatório de todos os fundos disponíveis.

# **TODO** :pushpin:

> Documentar problema :heavy_check_mark:

> Configurar ambiente :heavy_check_mark:

> Script1 código inicial :heavy_check_mark:

> Script2 código inicial :warning:

> Escrever testes :warning:

> Refatorar Script1 :warning:

> Refatorar Script2 :warning:

> API Bônus:warning:

> Revisar documentação :warning:

# **Iniciando o projeto** :rocket:

## **Docker**

### Crie seu container e execute os scripts

    # Cria o container
    docker build -t py-container . 

    # Entre no contexto do container
    docker run -it py-container bash
    
    # Execute o scripts 
    python script01.py <diretório> YYYYMM

    python script02.py YYYYMM <diretório> CNPJ0 CNPJ1 CNPJ2 CNPJ3


## **Testes** :label:

    Implementar depois de definir todo escopo do código

# **Bônus** :checkered_flag:

### Ao executar

    docker run -it py-container

### Uma API com funcionalidades semelhantes aos scripts do desafio é servida em

    # API
    localhost:8080

    # DOCS
    localhost:8080/docs
