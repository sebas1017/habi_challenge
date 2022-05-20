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



RESPUESTAS DUDAS:


    RESPUESTA DUDA 1 y2:
    en primera instancia opte por no realizar procedimiento almacenado ya que esto agrega
    otra capa en la base de datos que debe ser administrada , por lo que he realizado el respectivo QUERIE SQL que valida los datos de acuerdo a los requerimientos de la prueba es decir , que solo traiga los estados pre_venta, en_venta, vendido que no contengan valores nulos o vacios y que las propiedades tengan un status_id ya que existen registros de propiedades en la tabla property que no tienen relacion con la tabla status_history por lo que esas no serian propiedades validas , todas estas validaciones las realiza el querie y una vez ejecutada con estos datos limpios de retorno , los administro desde python.
    
    una vez teniendo los  datos limpios en python opte por usar la libreria pandas  para convertir estos datos en un dataframe y filtrarlos dependiendo de los requisitos del usuario  , los cuales llegan a traves del metodo POST en la API, lo cual es mejor que 
    modificar el QUERIE SQL dependiendo de los filtros ya que el dataframe es mas eficiente.


    RESPUESTA DUDA 3:
    para el 2 microservicio debo crear 2 tablas adicionales para romper la relacion que existe
    entre usuario - propiedades en cuanto a dar likes , ya que 1 usuario puede tener muchas propiedades con like pero 1 propiedad solo puede tener 1 like por usuario unico
    es decir que un usuario no puede dar "Like" a una misma propiedad 2 veces ya que eso seria
    "Unlike"   y de esta forma he diseñado el diagrama

    COMENTARIO ADICIONAL:
    opte por utilizar FastAPI ya que es mucho mas comodo en cuanto al manejo de errores,conexiones  y pruebas unitarias con pytest que utilizar la clase simpleHTTP.server de python para crear la API :)