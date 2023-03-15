# MarkoPolo

Pequeño y liviano asistente para linux escrito en python.
Es una version modificada del antiguo [markopolo](https://github.com/argonarch/Markopolo-KDE), que trae con sigo cambios importantes en la estructura, manejo de datos, formas de comunicacion y simplificado del codigo python antiguo.

Tambien corre sin necesidad de google-chrome haciendo uso de algunas minimas dependencias

Incluye:

- palabra de activacion (Markopolo)
- reconocmiento de voz (usando el servicio de google o azure)
- comandos personalizables mediante scripts de bash 

### Historia:

Desde hace mucho tiempo he querido tener un asistente al cual le pueda mandar intrucciones que ejecuten comandos en linux, lamentablemente los asistentes virtuales mas famosos (Google Assistant, Alexa, Siri) no comprenden esta funcion por medio nativo. Navegando por github para encontrar algun proyecto que este afines a mi necesidad encontre [markopolo](https://github.com/jazx/markopolo) de jazx un proyecto que me fascino su concepto y facilidad de uso, con el tiempo las grandes ideas de jazx dieron lugar al nacimiento de [trinity](https://github.com/jazx/trinity) el cual fue una gran mejora en funcionamiento a la version anterior, con ello me di a la tarea de mejorar y simplificar el proyecto, seguiendo el legado de jazx

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

La suma de estos filtros nos daran la direccion exacta del archivo bash que queremos ejecutar

### Instalacion:



sudo apt install python3-pip git libatlas-base-dev screen bash portaudio



Para facilidad del usuario se decidio crear un instalador automatico que se instala con el siguiente comando:

        curl -s "https://raw.githubusercontent.com/argonarch/trinity/main/easy-install.sh" | bash

Por defecto el repositorio se instalara en la carpeta /home/"su usuario"/

El cliente utiliza "Porcupine" como detector de palabra de activar y para poder utilizalo de debe crear una cuenta en [Picovoice](https://console.picovoice.ai/) e ingresar la llave de acceso que te proporcionan dentro del archivo **/Marko_Polo/client/hotword.py** (en el archivo se encuentra una indicacion de donde se debe pegar la llave)

Para ejecutar y detener el programa debe inicializar los siguientes archivos dentro de la carpeta Marko_Polo:

        ./run_trinity.sh                     (para iniciar el asistente)
        ./stop_trinity.sh                    (para detener el asistente)

Si tienes algun problema en el proceso de Instalacion e Ejecucion puedes comunicarlo [aqui](https://github.com/argonarch/Marko_Polo/issues/new) y estare contestandolo lo mas pronto posible

### Tecnologias

Las tecnologias que se usan en MarkoPolo son:

- Python (para la programacion general) 
- Json (para la escritura de los diccionarios)
- Bash (para los comandos que se van a ejecutar)
- MQTT (para la comunicacion via red o local entre cliente-servidor)
- PostgreSQL
- Docker

### Notas Finales

El proyecto, aunque ahora mismo se encuentra funcional, aun esta en pañales y se esperan nuevas fucionalidades a futuro, si estas interesado en dar tu grano de arena o tu piedra de 2 kilos al proyecto no lo dudes, la ayuda siempre es bienvenida y aceptada para todos 

### Contacto

Whatsapp: +54 1122559077

Telegram: +54 1122559077 o https://t.me/argonarch

Mail: argonarchy@gmail.com
