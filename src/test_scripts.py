from script1 import *
from script2 import *

'''
    A maioria das funções precisam ser refatoradas
    afim de terem retornos a serem validados
'''

# Script 1 1/4 TESTES ESCRITOS
def test_templating():
    '''
        testa a funcão templating
    '''
    t = ('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202003.csv', 'inf_diario_fi_202003.csv')
    assert t == templating('202003')


def test_require_data():
    pass


def test_stream_data():
    pass


def test_flow_definer():
    pass


# Script 2 2/6 TESTE ESCRITOS
def test_trunc():
    assert 2.33 == trunc(2.33333, 2)


def test_all_cnpjs():
    pass


def test_quota_price_variation():
    assert quota_price_variation(10,20) == float(100)


def test_analize_data():
    pass


def test_make_html():
    pass


def test_flow_definer_two():
    pass
