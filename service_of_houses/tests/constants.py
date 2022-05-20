INVALID_FILTERS_MESSAGE = {'message': 'No has ingresado ningun filtro , si deseas ver el total de los datos favor ejecutar el endpoint /all_houses gracias y favor verificar que todos los filtros ingresados (al menos debe ser uno) sean de tipo string '}
RESOURCE_NOT_FOUND_MESSAGE = {'message': 'el recurso solicitado no existe'}

mock_payload_invalid_filters= {
                "years": [2020],
                "cities": ["pereira"],
                "status": []
                }

mock_payload_correct_filter_1= {
                "years": ["2020"],
                "cities": ["pereira"],
                "status": []
                }



mock_filter_function_1= [("years", [2020]), ( "cities", ["pereira"]),("status", []) ]
mock_filter_function_2 = [("years", ["2020"]), ( "cities", ["pereira"]),("status", []) ]
mock_filter_function_3 = [("years", []), ( "cities", []),("status", []) ]
mock_filter_function_4 = [("years", [""]), ( "cities", [""]),("status", [""]) ]