import socket
import dicc_json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

while True:
    print('Esperando Conexion')
    connection, client_address = sock.accept()
    try:
        print('conectado a: ', client_address)

        while True:
            frase = connection.recv(1024).decode('utf-8')
            print('Frase recibida %s'%frase)
            if frase:
                comprobacion = 'Resivido'
                print('enviando confirmacion')
                connection.send(comprobacion.encode('utf-8'))
                dicc_json.entrada(frase)
            else:
                print('no data from', client_address)
                break

    finally:
        connection.close()
