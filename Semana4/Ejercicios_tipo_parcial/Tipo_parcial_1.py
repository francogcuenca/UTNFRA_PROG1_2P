# 1-Debemos realizar la carga de 5(cinco) productos de prevención de contagio
# debo obtener los siguientes datos: el tipo (validar "barbijo" , "jabón" o "alcohol", “guardapolvo”, “guantes”) , el precio (validar entre 100 y 300), la cantidad de unidades (no puede ser 0 o negativo y no debe superar las 1000 unidades), la Marca y el fabricante.
# Se debe Informar al usuario lo siguiente:
# a) Del más caro de los Barbijos, la cantidad de unidades y el fabricante
# b) Del ítem con más
# más unidades, el fabricante
# c) Cuántas unidades de jabones hay en total
# Danilo Barbosa Fernandez
# 21:27
#marca y fabricante cualquiera piden 5 nada mas


TIPO_BARBIJO = "barbijo"
TIPO_JABON = "jabon"
TIPO_ALCOHOL = "alcohol"
TIPO_GUARDAPOLVO = "guardapolvo"
TIPO_GUANTES = "guantes"


PRRECIO_MAX = 300
PRECIO_MIN = 100

CANTIDAD_MAXIMA = 1000
CANTIDAD_MINIMA = 1

contador_productos = 0

while contador_productos<5:
    tipo_prod = input('Ingrese el tipo de producto:,{TIPO_BARBIJO}, {TIPO_JABON},{TIPO_ALCOHOL},{TIPO_GUARDAPOLVO},{TIPO_GUANTES}')
    while tipo_prod != TIPO_ALCOHOL and tipo_prod != TIPO_BARBIJO and tipo_prod != TIPO_GUANTES and tipo_prod != TIPO_GUARDAPOLVO and tipo_prod != TIPO_JABON:
        tipo_prod = input('¡¡ERROR!!Ingrese UN tipo de producto de la lista:,{TIPO_BARBIJO}, {TIPO_JABON},{TIPO_ALCOHOL},{TIPO_GUARDAPOLVO},{TIPO_GUANTES}')
    
    precio_prod = round(float(input('Ingrese el precio (minimo $100, maximo 300) :$')), 2)
    while precio_prod<=300 and precio_prod>=100:
        precio_prod = round(float(input('¡¡ERROR!!Ingrese un precio dentro del rango (minimo $100, maximo 300) :$')), 2)

    cantidad = int(input('Ingrese la cantidad (entre 1 y 1000 unidades): '))
    while not(cantidad < CANTIDAD_MAXIMA and cantidad > CANTIDAD_MINIMA):
        cantidad = int(input('¡¡ERROR!!Ingrese la cantidad nuevamente (entre 1 y 1000 unidades): '))
    
    marca = input('Ingrese la marca: ')
    fabricante = input('Ingrese el fabricante: ')



