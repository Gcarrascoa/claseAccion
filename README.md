# claseAccion
#Crear una clase en Python (Python 3.6 en adelante) que permita representar una acción de la bolsa.

autor: Giovanni Carrasco

Librerias utilizadas : datetime

Version Python : 3 

Nombre de la clase: Accion

parametros:

nemotecnico (nombre de la acción, por ejemplo GOOGL)
ultimo_precio (ultimo precio de la accion, por ejemplo 123.34)
precios_historicos (diccionario que represente los precios de fechas anteriores.)
Cada elemento del diccionario tiene el siguiente formato de llave-valor, 
llave: string que representa lafecha en formato ‘YYYY-MM-DD’
valor: el precio (numero flotante) de la acción para ese dia

(se consideran que todos los precios estan en pesos chilenos, asi que no hay que considerar la moneda.)

metodos:

constructor init(): debe iniciar la acción con el nemotecnico. Se puede dar un ultimo_precio como parámetro opcional.
ejemplo: accion = Accion(“GOOGL”)
ejemplo accion = Accion(“GOOGL”, 120.01 )
actualizar_ultimo_precio : actualiza el ultimo_precio del objeto.
ejemplo: accion.actualizar_ultimo_precio( 130.01 )
agregar_precio_histórico: agrega un nuevo precio al diccionario de precios_historicos, indicando fecha y precio.
ejemplo: accion.agregar_precio_historico( “2019-07-28”, 123.067 )
obtener_precio_para_fecha: obtiene el precio desde precios_historicos para la fecha indicada. Si la fecha no existe en el diccionario debe devolver 0.
ejemplo: accion.obtener_precio_para_fecha(“2019-07-20”)
obtener_rentabilidad: revuelve la rentabilidad de la acción. Esto se calcula usando el precio MAS ANTIGUO SEGUN FECHA de precios_historicos y el ultimo_precio, usando la siguiente formula:
rentabilidad = (ultimo_precio/precio_mas_antiguo) -1
si no hay ultimo_precio o su valor es cero, se debe considerar el valor más actual de precios_historicos.
si no hay precios en precios_historicos, la rentabilidad es 0.
ejemplo: accion.obtener_rentabilidad()
