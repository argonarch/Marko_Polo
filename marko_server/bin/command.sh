INGRESO=$1

TARGET=`echo $INGRESO | sed s/^.*internet//g`

firefox --new-tab "https://www.google.com/search?q=$TARGET" &

bash ./bin/trinity-message "Internet" "Buscando en google"