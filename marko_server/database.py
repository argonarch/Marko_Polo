import psycopg2

def database(ejecutador):
    connection = psycopg2.connect(
    host = 'localhost',
    user = 'Argon',
    password = 'Hola',
    database = 'Marko'
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
    vert = database(acciones)
    list = []
    for row in vert:
        list.append(row[0])
    return list

def list_activators(accion):
    acciones = "SELECT activador FROM sectores WHERE accion='%s'"%accion
    return listador(acciones)

def word_sinonimo(accion):
    acciones = "SELECT sinonimo FROM sectores WHERE accion='%s' "%accion
    return listador(acciones)

def word_activador(accion):
    acciones = "SELECT sinonimo FROM activadores WHERE clave='%s'"%accion
    return listador(acciones)

def word_especial(accion):
    acciones = "SELECT sinonimo FROM especial WHERE clave='%s'"%accion
    return listador(acciones)

def listador(acciones):
    vert = database(acciones)
    for row in vert:
        acti = row[0]
    return acti


#sisi = 'a_go'
#hola = word_activador(sisi)
#print(type(hola))