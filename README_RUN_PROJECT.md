API houses :)


![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/fastapi.png?raw=true)


![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/docker.jpeg?raw=true)

![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/heroku.png?raw=true)

# REQUISITOS
    - Tener docker y docker-compose instalado

# INSTALACION

Para ejecutar el proyecto he usado docker-compose para su facil ejecucion
si se desea ejecutar el proyecto ejecutar el siguiente comando en la raiz del proyecto
al nivel del archivo docker-compose.yml

    docker-compose up




esto permitira que se descargue la imagen de python y construya el dockerfile del servicio
de casas y cuando el proceso termine podra ver corriendo el proyecto en el siguiente url

http://localhost:8000/docs


![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/api_run.png?raw=true)


para ejecutar los tests del proyecto ejecutar el comando
    docker-compose run houses_api_service pytest tests

si desea ejecutar el proyecto sin docker-compose solo desplazarse hasta la ruta
/service_of_houses   y crear un entorno virtual en ella con el siguiente comando

    python3 -m venv venv  

luego activar el entorno virtual

    source venv/bin/activate

y posteriormente despues de activarlo ejecutar el script main.py

    python3 main.py

si desea ejecutar los tests , solo ejecutar el siguiente comando:
    pytest tests

y podra ver en ejecucion el proyecto en el url http://localhost:8000/docs


la documentacion acerca de como usar la API se encuentra en el directorio
/service_of_houses/frontend_parameters/DOC.md


# Despliegue en heroku
    - debes tener una cuenta en heroku creada con anterioridad y tener el Cliente de heroku
    instalado para ejecutar comandos de heroku

    heroku login
    heroku container:login
    heroku create nombre_app  #o el nombre que desee
    heroku container:push web -a  nombre_app
    heroku container:release web -a  nombre_app  #esto despliega


# PUNTO 2 PRUEBA
    la documentacion acerca del diagrama y el script sql de las tablas que se debia realizar
    se encuentra en la carpeta microservicio_2_diagrama


gracias :)

