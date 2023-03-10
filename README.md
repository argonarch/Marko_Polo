# MarkoPolo
Pequeño y liviano asistente para linux escrito en python.
Es una version modificada del antiguo markopolo, que trae con sigo cambios importantes en la estructura, aplicando json, mqtt y simplificando el codigo python antiguo.
<br>
<br>
Tambien corre sin necesidad de google-chrome haciendo uso de algunas minimas dependencias

Incluye
- palabra de activacion (Markopolo)
- reconocmiento de voz (usando el servicio gratuito de google)
- comandos personalizados configurados mediante scripts de bash


### Funcionamiento:
MarkoPolo se divide en 2 partes
- Cliente: Es el encargado de detectar la palabra de activacion, detectar la frase que dice el usario y enviar la frase juntos con otros datos*1 al servidor mediante mqtt
- Servidor: Se encarga de recivir los datos proporcionados por el cliente, procesarlos y ejecutar los comandos correspondientes que se configuraron para la frase 

El servidor esta programado para separar la frase entrante en 3 filtros:

- El primero detecta si la frase se trata de un comando especial (palabras inpronunciables seleccionados), sirve para la comunicacion directa de un cliente y servidor saltandose los siguientes filtros

- El segundo sirve para detectar el "sector" al cual pertenece la frase, sirve para detectar el contexto de la frase por ejemplo: 
si le pedimos al servidor "bajar volumen" y "bajar archinvo" la palabra "bajar" cambiara de significado para el programa dependiendo si pertenece al sector "volumen" o "archivo" y ejecutara comandos diferentes

- El tercer filtro detecta todas las palabras claves escritas en los diccionarios json y los descarta segun pertenezcan al sector definido o no, 

La suma de estos filtros nos daran la direccion exacta del archivo bash que queremos ejecutar


### Instalacion:

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


### Creditos

Cabe aclarar que todo el proyecto no hubiera sido posible sin la ayuda de [Jazx](https://github.com/jazx) y su proyecto [Trinity](https://github.com/jazx/trinity) que dio las bases con las que simentar este proyecto

### instalar

sudo apt install python3-pip git python3-pyaudio libatlas-base-dev screen bash


### Notas Finales

El proyecto, aunque ahora mismo se encuentra funcional, aun esta en pañales y se esperan nuevas fucionalidades a futuro, si estas interesado en dar tu grano de arena o tu piedra de 2 kilos al proyecto no lo dudes, la ayuda siempre es bienvenida y aceptada para todos 

### Contacto

Whatsapp: +54 1122559077

Telegram: +54 1122559077 o https://t.me/argonarch

Mail: argonarchy@gmail.com
