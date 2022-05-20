  
los parametros que deben ser enviados desde el frontend hacia 
el endpoint   http://localhost:8000/api/v1/filter_data_houses atraves de POST
deben tener la siguiente estructura y los tipos de datos indicados
en cada campo se pueden aplicar multiples filtros y en una sola consulta,
si un campo queda vacio y los demas tienen valor entonces ese campo no sera tomado
en cuenta para el filtrado y solo se tendran en cuenta los filtros que se usaron.
{
    "years": [
      "string"
    ],
    "cities": [
      "string"
    ],
    "status": [
      "string","string","string"
    ]
  }

  ejemplo de una peticion



  {
    "years": [
      "2020",
    ],
    "cities": [
      "pereira"
    ],
    "status": [
      "pre_venta","en_venta","vendido"
    ]
  }


  {
  "years": [
    "2020","2021"
  ],
  "cities": [
    "pereira"
  ],
  "status": [
    
  ]
}

#al no usar el filtro status se traen los datos con los filtros years y cities y todos los status: pre_venta, en_venta, vendido

si se envian los 3 filtros vacios la API controla el error y retorna un mensaje
al cliente , ya que al no usar los 3 filtros desea consultar todos los datos
para lo cual existe otro endpoint  http://localhost:8000/api/v1/all_houses el cual
solo requiere realizar una peticion de tipo GET

  {
  "years": [
   
  ],
  "cities": [
    
  ],
  "status": [
    
  ]