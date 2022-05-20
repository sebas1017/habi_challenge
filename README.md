

API houses :)



![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/fastapi.png?raw=true)


![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/docker.jpeg?raw=true)

![alt text](https://github.com/sebas1017/habi_challenge/blob/main/demo_image/heroku.png?raw=true)




Inicialmente, he decidido por utilizar las siguientes tecnologías para él
desarrollo de la prueba




FastAPI + Python

al no utilizar ORM he optado por realizar la consulta que permita
traer los datos limpios de la base de datos de acuerdo a las condiciones del documento
y luego de tener estos datos limpios, entonces filtrarlos desde Python dependiendo
de los filtros que solicite el usuario


Dudas iniciales:

    DUDA 1:
    se deben hacer varias validaciones entre las tablas para llegar a los datos finales que 
    son de valor por lo que no sé si optar por crear un procedimiento almacenado
    que realice todas estas validaciones en la base de datos y me entregue los datos finales en Python con un llamado a este procedimiento o realizar una consulta SQL que me entregue
    los datos totales limpios con sus respectivas validaciones de status, valores nulos y demás
    y luego filtrarlos desde Python dependiendo de los requisitos del usuario.


    DUDA 2:
    para el filtrado de los datos dependiendo de los filtros del usuario , al ser una consulta
    en formato string debido a que es SQL puro desde python modificar este string
    dependiendo de los datos del usuario me parece tedioso por lo que debo pensar en alguna
    forma de filtrar estos datos sin tener que modificar el querie_string


    DUDA: 3
    aun no tengo idea de como crear el modelo para el 2 microservicio :( pero
    ya veremos luego :)


RESPUESTAS DUDAS:


    RESPUESTA DUDA 1 y 2:
    en primera instancia opté por no realizar procedimiento almacenado, ya que esto agrega
    otra capa en la base de datos que debe ser administrada, por lo que he realizado el respectivo QUERIE SQL que válida los datos de acuerdo a los requerimientos de la prueba es decir, que solo traiga los estados pre_venta, en_venta, vendido que no contengan valores nulos o vacíos y que las propiedades tengan un status_id, ya que existen registros de propiedades en la tabla property que no tienen relación con la tabla status_history por lo que esas no serian propiedades válidas, todas estas validaciones las realiza el querie y una vez ejecutada con estos datos limpios de retorno, los administro desde Python.
    
    Una vez teniendo los  datos limpios en Python, opté por usar la librería pandas  para convertir estos datos en un dataframe y filtrarlos dependiendo de los requisitos del usuario, los cuales llegan a través del método POST en la API, lo cual es mejor que 
    modificar el QUERIE SQL dependiendo de los filtros, ya que el dataframe es más eficiente.


    RESPUESTA DUDA 3:
    para el 2 microservicio debo crear 2 tablas adicionales para romper la relación que existe
    entre usuario - propiedades en cuanto a dar likes, puesto que 1 usuario puede tener muchas propiedades con like, pero 1 propiedad solo puede tener 1 like por usuario único
    es decir, que un usuario no puede dar "Like" a una misma propiedad 2 veces, puesto que eso seria "Unlike"  y de esta forma he diseñado el diagrama

    COMENTARIO ADICIONAL:
    opte por utilizar FastAPI, ya que es mucho más cómodo en cuanto al manejo de errores, conexiones  y pruebas unitarias con pytest que utilizar la clase simpleHTTP.server de Python para crear la API :)




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
    instalado para ejecutar comandos de heroku, y moverse a la ruta service_of_houses
    y al nivel del Dockerfile ejecutar los siguientes comandos

    heroku login
    heroku container:login
    heroku create nombre_app  #o el nombre que desee
    heroku container:push web -a  nombre_app
    heroku container:release web -a  nombre_app  #esto despliega


# PUNTO 2 PRUEBA
    la documentacion acerca del diagrama y el script sql de las tablas que se debia realizar
    se encuentra en la carpeta microservicio_2_diagrama


gracias :)

