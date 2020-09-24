from script1 import templating

from script2 import trunc

# Script 1
def test_templating():
    t = ('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202003.csv', 'inf_diario_fi_202003.csv')
    assert t == templating('202003')

# Script 2
def test_trunc():
    assert 2.33 == trunc(2.33333, 2)

