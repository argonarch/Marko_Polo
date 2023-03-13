import datadb
import pytest
from collections import Counter

def test_create_list():
    assert  isinstance(datadb.create_list(),list)

@pytest.mark.parametrize(
    'sector, lista_activadores',
    [
        ('MUSIC',['a_stop', 'a_search', 'o_music', 'o_volume', 'a_go', 'a_up', 'a_down']),
        ('IMAGES',['a_go','a_search','o_image'])
    ]
)

def test_list_activators(sector,lista_activadores):
    funcion = datadb.list_activators(sector)
    assert  isinstance(funcion,list)
    assert  Counter(funcion) == Counter(lista_activadores)

@pytest.mark.parametrize(
    'sector, lista_sinonimos',
    [
        ('MUSIC',['musica', 'cancion', 'album', 'disco']),
        ('INTERNET', ['internet','google','navegador'])
    ]
)

def test_word_sinonimo(sector,lista_sinonimos):
    funcion = datadb.word_sinonimo(sector)
    assert  isinstance(funcion,list)
    assert  Counter(funcion) == Counter(lista_sinonimos)

@pytest.mark.parametrize(
    'activador, lista_sinonimos',
    [
        ('o_light',['luz', 'iluminacion', 'luces']),
        ('o_music', ['musica','cancion','album','disco'])
    ]
)

def test_word_activador(activador,lista_sinonimos):
    funcion = datadb.word_activador(activador)
    assert  isinstance(funcion,list)
    assert  Counter(funcion) == Counter(lista_sinonimos)

@pytest.mark.parametrize(
    'sector, activadores, comando',
    [
        ('VOLUME',"'a_up','o_volume'",'~/.config/dunst/scripts/volume up')
    ]
)

def test_encontar_comando(sector, activadores, comando):
    funcion = datadb.encontar_comando(sector,activadores)
    assert  isinstance(funcion,str)
    assert  funcion == comando

