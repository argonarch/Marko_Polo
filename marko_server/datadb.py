import psycopg2
from decouple import config

def database(ejecutador):
    connection = psycopg2.connect(
    host = config('Postgresql_Host'),
    user = config('Postgresql_User'),
    password = config('Postgresql_Pass'),
    database = config('Postgresql_DB')
    )

    #print('conectado')

    buscador = connection.cursor()

    buscador.execute("%s"%ejecutador)
    vert = buscador.fetchall()
    #print(vert)

    connection.close()
    #print('conexion terminada')
    
    return vert

def create_list():
    acciones = "SELECT accion FROM sectores WHERE accion!='SPECIAL'"
    return listador_S(acciones)

def list_activators(accion):
    acciones = "select clave from activadores where id in (select activa from activadores_sectores where sector=(select id from sectores where accion='%s'))"%accion
    return listador_S(acciones)

def word_sinonimo(accion):
    acciones = "SELECT sinonimo FROM sectores WHERE accion='%s' "%accion
    return listador(acciones)

def word_activador(accion):
    acciones = "SELECT sinonimo FROM activadores WHERE clave='%s'"%accion
    return listador(acciones)

def encontar_comando(sector,activadores):
    acciones ="select comando from comandos where sector=(select id from sectores where accion='%s') and id in (select comando from comandos_activadores where activa in (select id from activadores where clave in (%s)) group by comando having count(comando) > 1)"%(sector,activadores)
    return listador(acciones)

def comando_special(nombre):
    acciones = "select comando from comandos where nombre='%s'"%nombre
    return listador(acciones)

def listador(acciones):
    vert = database(acciones)
    for row in vert:
        acti = row[0]
    return acti

def listador_S(acciones):
    vert = database(acciones)
    list = []
    for row in vert:
        list.append(row[0])
    return list




