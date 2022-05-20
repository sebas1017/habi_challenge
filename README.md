Inicialmente , he decidido por utilizar las siguientes tecnologias para el
desarrollo de la prueba

FastAPI + Python

al no utilizar ORM he optado por realizar la consulta que permita
traer los datos limpios de la base de datos de acuerdo a las condiciones del documento
y luego de tener estos datos limpios , entonces filtrarlos desde python dependiendo
de los filtros que solicite el usuario


Dudas iniciales:

    DUDA 1:
    se deben hacer varias validaciones entre las tablas para llegar a los datos finales que 
    son de valor por lo que no se si optar por crear un procedimiento almacenado
    que realice todas estas validaciones en la base de datos y me entregue los datos finales en python con un llamado a este procedimiento o realizar una consulta SQL que me entregue
    los datos totales limpios con sus respectivas validaciones de status valores nulos y demas
    y luego filtrarlos desde python dependiendo de los requisitos del usuario.


    DUDA 2:
    para el filtrado de los datos dependiendo de los filtros del usuario , al ser una consulta
    en formato string debido a que es SQL puro desde python modificar este string
    dependiendo de los datos del usuario me parece tedioso por lo que debo pensar en alguna
    forma de filtrar estos datos sin tener que modificar el querie_string


    DUDA: 3
    aun no tengo idea de como crear el modelo para el 2 microservicio :( pero
    ya veremos luego :)