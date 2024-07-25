# Realizar el algoritmo que permita ingresar los datos de una compra de ingredientes
# para preparar comida al por mayor , hasta que el cliente quiera:
# peso (entre 10 y 1000)en kilo,
# precio por kilo (más de cero ),
# tipo validad("v";"a";"m")(vegetal,animal o mezcla )
# Si compro más de 100 kilos en total tenes 15% de descuento sobre el total a pagar.
# Si compro más de 300 kilos en total tenes 25% de descuento sobre el total a pagar.

# Se debe Informar al usuario lo siguiente:
# a)El importe total a pagar , bruto sin descuento y...
# b)el importe total a pagar con descuento(solo si corresponde)
# d)Informar el tipo de alimento más caro.
# f)El promedio de precio por kilo en total.

# Flags
flag_compra = True

# Contadores
cant_ingredientes = 0

# Acumuladores
acum_precio = 0
acum_peso = 0

# Variables
precio_mas_caro = None
tipo_mas_caro = None

print('\nBienvenido al cotizador de ingredientes para preparar comida al por mayor.')

# Input y validaciones
while flag_compra == True:
    peso = float(input('\nIngrese el peso del ingrediente en kilos (mayor a 10 y menor que 1000): '))
    while peso<10 or peso>1000:
        peso = float(input('\n¡¡ERROR!! Peso no válido, reingrese el peso del ingrediente en kilos (mayor a 10 y menor que 1000): '))

    precio_kilo = float(input('\nIngrese el precio del ingrediente por kilo en número: $'))
    while precio_kilo<=0:
        precio_kilo = float(input('\n¡¡ERROR!! Precio no válido, reingrese el precio del ingrediente por kilo en número: $'))
    
    tipo_variedad = (input('\nIngrese el tipo de variedad: vegetal (v), animal(a) o mezcla (m): ')).upper()
    while not(tipo_variedad=="V" or tipo_variedad=="A" or tipo_variedad=="M"):
        tipo_variedad = (input('\n¡¡ERROR!! Tipo de variedad no válido, reingrese el tipo de variedad: vegetal (V), animal(A) o mezcla (M): ')).upper()

    continuar_compra = (input('\nDesea seguir comprando ingredientes (si/no): ')).upper()
    while not(continuar_compra == "SI" or continuar_compra == "NO"):
        continuar_compra = (input('\n¡¡ERROR!! Entrada incorrecta, desea seguir comprando ingredientes (si/no): ')).upper()
    
    # Chequeo cambio de flag
    if continuar_compra == "NO":
        flag_compra = False
    
    # Acumulación para total
    acum_precio = acum_precio + precio_kilo * peso
    acum_peso = acum_peso + peso

    # Definir tipo de alimento más caro
    if precio_mas_caro == None or precio_mas_caro<precio_kilo:
        precio_mas_caro = precio_kilo
        tipo_mas_caro = tipo_variedad
    match tipo_mas_caro:
        case "V":
            tipo_mas_caro = "vegetal"
        case "A":
            tipo_mas_caro = "animal"
        case "M":
            tipo_mas_caro = "mezcla"

# Informe
print('El importe bruto a pagar es de: $',str(round(acum_precio, 2)))

if acum_peso>100 and acum_peso<300:
    precio_con_descuento = acum_precio - acum_precio * 0.15
    print('El importe total con descuento es de: $',str(round(precio_con_descuento, 2)))

elif acum_peso>300:
    precio_con_descuento = acum_precio - acum_precio * 0.25
    print('El importe total con descuento es de: $',str(round(precio_con_descuento, 2)))

print('El alimento más caro es del tipo',tipo_mas_caro)

precio_promedio = round((acum_precio/acum_peso), 2)
print('El promedio de precio por kilo total es de: $', str(precio_promedio))