El archivo load_data.sql contiene informacion para:
-Crear los schemas
-Crear funciones que ayudan a los comandos load data infile
-Llama los load data para cada archivo csv

Si no fuera porque la consigna dicta esto, hubiera creado 3 archivos distintos para su modularizacion

Cree la funcion:
-convert_time_to_datetime
Para corregir los datetimes que venian de los csv:
La logica de la funcion es convetir en segundos las horas del csv, y restarle ese valor al today date
14:01.7 --> 2014-01-07 00:00:00
