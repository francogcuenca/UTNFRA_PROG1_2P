'''Usuarios vendedores de MercadoLibre
Cargar 10 usuarios/vendedores de MercadoLibre con sus respectivas
publicaciones.
● Los datos que se cargarán son:
● Nombre de usuario
● Edad (validar)
● Cantidad de productos (validar-número entero positivo).
● Número de publicaciones (validar-número entero positivo, hasta 1000).
● Tipo ("producto", "servicio", "subasta")
● Cuenta activa ("si", "no")
Se necesita saber
Tema A:
1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo
“producto”, cuya edad esté entre 25 y 35 años inclusive.
2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
3. Porcentaje de publicaciones de tipo subasta.
4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron
del tipo “producto”.
5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre
“activa”.'''

# Constantes
EDAD_MAX_REQ=25
EDAD_MIN_REQ=35
PRODUCTO="producto"
SERVICIO="servicio"
SUBASTA="subasta"

# Flags
cont_usuarios = 0


# Contadores
cont_prod_activa = 0
cont_serv_activa = 0
cont_subas_activa = 0
activa_25_35= 0

cont_subasta = 0
cont_publicacion_subasta =0
cont_producto = 0
cont_servicio = 0


# Acumuladores
usuario_menor_edad_500= None
edad_tipo_producto = 0
total_publicaciones = 0

# Variables
nombre_menor_edad_500=None
tipo_menor_edad_500=None

while cont_usuarios<4:
    # Input y validación
    nombre = input('\nIngrese el nombre del usuario vendedor de Mercadolibre: ')

    edad = int(input('\nIngrese la edad del vendedor en número: '))
    while not(edad>0):
        edad = int(input('¡¡ERROR!! Edad inválida, reingrese la edad del vendedor en número: '))

    cant_productos = int(input('\nIngrese la cantidad de productos en número: '))
    while cant_productos<0:
        cant_productos = int(input('¡¡ERROR!! Cantidad inválida, reingrese la cantidad de productos en número: '))

    cant_publicaciones = int(input('\nIngrese la cantidad de publicaciones del vendedor en número: '))
    while not(cant_productos<=1000):
        cant_publicaciones = int(input('\n¡¡ERROR!! Reingrese la cantidad de publicaciones del vendedor en número: '))

    tipo = (input(f'\nTipos de publicación disponibles: \n{PRODUCTO}\n{SERVICIO}\n{SUBASTA}\nIngrese el tipo de publicacion: ')).upper()
    while not(tipo=="PRODUCTO" or tipo=="SERVICIO" or tipo=="SUBASTA"):
        tipo = (input(f'¡¡ERROR!!Tipo de publicación inválido, reingrese un tipo perteneciente a la lista: ')).upper()

    activa = (input(f'\nLa cuenta se encuentra activa? (si/no): ')).upper()
    while not(activa=="SI" or activa=="NO"):
        activa = (input(f'¡¡ERROR!!Entrada incorrecta, La cuenta se encuentra activa? (si/no): ')).upper()

    total_publicaciones +=cant_publicaciones
    cont_usuarios += 1  


    if activa == "SI":
        match tipo:
            case "PRODUCTO":
                cont_prod_activa += 1
            case "SUBASTA":
                cont_subas_activa += 1
            case "SERVICIO":
                cont_serv_activa += 1
                
        if edad>25 and edad<=35:
            activa_25_35 += 1
    
    if cant_publicaciones>500:
        if usuario_menor_edad_500==None or usuario_menor_edad_500>edad:
            usuario_menor_edad_500 = edad
            nombre_menor_edad_500 = nombre
            tipo_menor_edad_500 = tipo

    match tipo:
        case "SUBASTA":
            cont_subasta += 1
            cont_publicacion_subasta= cant_publicaciones

        case "PRODUCTO":
            edad_tipo_producto += edad
            cont_producto +=1
        
        case "SERVICIO":
            cont_servicio += 1
    
'''
1. Cantidad de usuarios con la cuenta activa cuyo producto sea del tipo
“producto”, cuya edad esté entre 25 y 35 años inclusive.
2. Nombre y tipo del usuario de menor edad con más de 500 publicaciones.
3. Porcentaje de publicaciones de tipo subasta.
4. Mostrar el promedio de edad de los usuarios cuyas publicaciones fueron
del tipo “producto”.
5. Determinar el tipo con más publicaciones, cuya cuenta se encuentre
“activa”.'''


print(f'Hay {activa_25_35} usuarios con la cuenta activa, cuya edad está entre 25 y 35 años inclusive.')

if not(usuario_menor_edad_500 == None):
    print(f'El usuario {nombre_menor_edad_500} es el usuario con menor edad con más de 500 publicaciones del tipo {tipo_menor_edad_500}.')

porcentaje_subasta = round(cont_publicacion_subasta/total_publicaciones, 2)
if cont_subasta>0:
    print(f'Un {porcentaje_subasta}% de las publicaciones es del tipo SUBASTA.')

if cont_producto>0:
    prom_edad_producto = round(edad_tipo_producto/cont_producto, 2)
    print(f'El promedio de edad de los usuarios de tipo PRODUCTO es de {prom_edad_producto} años.')

if cont_producto>cont_subasta and cont_producto>cont_servicio:
    print('El tipo con más publicaciones es PRODUCTO.')
elif cont_servicio>cont_producto and cont_servicio>cont_subasta:
    print('El tipo con más publicaciones es SERVICIO.')
elif cont_subasta>cont_producto and cont_subasta>cont_servicio:
    print('El tipo con más publicaciones es SUBASTA.')
elif cont_producto==cont_servicio:
    print('El tipo con más publicaciones está empatado entre PRODUCTO Y SERVICIO.')
elif cont_producto==cont_subasta:
    print('El tipo con más publicaciones está empatado entre PRODUCTO Y SUBASTA.')
elif cont_subasta==cont_servicio:
    print('El tipo con más publicaciones está empatado entre SUBASTA Y SERVICIO.')







    

