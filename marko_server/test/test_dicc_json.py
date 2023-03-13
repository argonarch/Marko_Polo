import dicc_json
import pytest
from collections import Counter

@pytest.mark.parametrize(
    'frase,modo,claves,resultado',
    [
        ('subir volumen',1,['VOLUME','MUSIC','SPECIAL'],'VOLUME'),
        ('subir volumen',2,['a_stop', 'a_search', 'o_volume', 'm_outside', 'm_inside', 'm_up', 'm_down', 'a_go', 'a_down', 'a_up'],['a_up', 'o_volume'])
    ]
)

def test_tagcreator(frase,modo,claves,resultado):
    assert Counter(dicc_json.tagcreator(frase,modo,claves)) == Counter(resultado)

@pytest.mark.parametrize(
    'frase',
    [
        ('subir volumen')
    ]
)
def test_entrada(frase):
    assert dicc_json.entrada(frase) == 0

