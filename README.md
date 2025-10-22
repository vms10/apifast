Con el comando  fastapi dev main.py levantamos el servidor
Si lo probas localmente: url + nombre del endpoint (hola)
http://127.0.0.1:8000/hola
Ahi te devuelve el mensaje


desde un google si pones:
http://127.0.0.1:8000/files/prueba45.txt

te devuelve el contenido de ese archivo

####################################
Desde la terminar en Windows el comando es: 
curl.exe -X GET "http://127.0.0.1:8000/files"
 curl.exe -X 'GET' 'http://127.0.0.1:8000/files/prueba45.txt'

curl.exe -X 'POST' 'http://127.0.0.1:8000/files' -H 'Content-Type: application/json' -d '{"name": "test.txt", "content": "Este es un archivo de prueba"}' 




Para crear el requirements.txt
 pip list
 pip freeze > requirements.txt
 