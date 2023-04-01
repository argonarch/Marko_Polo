# MarkoPolo

Pequeño y liviano asistente para linux escrito en python.
Es una version modificada del antiguo [markopolo](https://github.com/argonarch/Markopolo-KDE), que trae con sigo cambios importantes en la estructura, manejo de datos, formas de comunicacion y simplificado del codigo python antiguo.

Tambien corre sin necesidad de google-chrome haciendo uso de algunas minimas dependencias

Incluye:

- palabra de activacion (Markopolo)
- reconocmiento de voz (usando el servicio de google o azure)
- comandos personalizables mediante scripts de bash 

### Funcionamiento:

Marko_Polo se divide en 3 partes

- Cliente: Es el encargado de procesar el audio entrante, detectar la oracion y enviarlo al servidor mediante mqtt o por medio local (sockets)
- Servidor: Se encarga de recibir los datos proporcionados por el cliente, procesar la oracion, detectar el contexto y palabras de claves y ejecutar los comandos correspondientes que se hayan configurado para la situacion
- Base de datos: En el se almacenan los palabras asociadas a las palabras claves y a los contextos, como tambien los comandos que seran ejecutados

El servidor esta programado para separar la frase entrante en 3 filtros:

- El primero detecta si la frase se trata de un comando especial, sirve para la comunicacion directa de un cliente y el servidor saltandose los filtros siguientes

- El segundo sirve para detectar el "sector" al cual pertenece la frase, sirve para detectar el contexto de la oracion por ejemplo:
  
  - Si tomamos como entrada: "reproducir musica pop", podemos asumir que el contexto de la oracion pasa por la "musica" 
  
  - Si tomamos como entrada: "buscar videos de musica para todos", podemos asumir que el contexto de la oracion pasa por la "videos"  

- El tercer filtro detecta todas las palabras claves definidas en el sector que se encuentren en la oracion 

El uso del 2do filtro radica en reducir numero de procesos al no tener que filtrar todas las palabras claves y evitar confuciones a la hora de saber que comando ejecutar, por ejemplo: si dieramos "buscar videos de como reproducir musica pop" el programa no sabria si tendria que reproducir una musica o buscar un video

Los filtros nos daran un texto que contiene el comando en bash que luego sera ejecutado

### Instalacion:

##### Pre paquetes

Las dependencias necesarias antes de la instalacion son:

`python pip git screen bash portaudio`



##### Copiar Git e Instalar paquetes python

```
git clone https://github.com/argonarch/Marko_Polo.git
cd Marko_Polo
./run.sh install
```

##### Establecer varibles

Editar el archivo .env_example, alli se deben establecer las variables establecidas y cambiar su nombre de `.env_example` a `.env`

##### Ejecutar

Commandos de iniciacion y detencion :

        ./run.sh start-home             (iniciar en modo home el asistente)
        ./run.sh start-cloud            (iniciar en modo cloud el asistente)
        ./run.sh stop                   (detener el asistente)

### Tecnologias

Las tecnologias que se usan en MarkoPolo son:

- Python (para la programacion general) 
- Json (para la escritura de los diccionarios)
- Bash (para los comandos que se van a ejecutar)
- MQTT (para la comunicacion via red o local entre cliente-servidor)
- PostgreSQL
- Docker

### Creditos

Cabe aclarar que todo el proyecto no hubiera sido posible sin la ayuda de [Jazx](https://github.com/jazx) y su proyecto [Trinity](https://github.com/jazx/trinity) que dio las bases con las que simentar este proyecto

### Notas Finales

El proyecto, aunque ahora mismo se encuentra funcional, aun esta en pañales y se esperan nuevas fucionalidades a futuro, si estas interesado en dar tu grano de arena o tu piedra de 2 kilos al proyecto no lo dudes, la ayuda siempre es bienvenida y aceptada para todos 

