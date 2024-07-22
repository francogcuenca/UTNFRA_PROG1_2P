# Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de comprar cada entrada:

# Al presionar el botón se deberá pedir la carga de los siguientes datos, hasta que el usuario lo desee:

# Los datos que deberás pedir para los ventas son:
#    * Nombre del comprador
#    * Edad (no menor a 16)
#    * Género (Masculino, Femenino, Otro)
#    * Tipo de entrada (General, Campo delantero, Platea)
#    * Medio de pago (Crédito, Efectivo, Débito)
#    * Precio de la entrada (Se debe calcular)

# Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida,el medio de pago y su precio correspondiente.

# * Lista de precios:
#        * General: $16000
#        * Campo:   $25000
#        * Platea:  $30000

# Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%.
# Al finalizar la carga, el programa deberá mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.

#_______________________________________________________________________________________________________________________________________

# Constantes
general = 16000
campo = 25000
platea = 30000

# Variables
ctrlCompra = 0


while ctrlCompra == 0:
    nombre = input('Ingrese su nombre completo: ')
    # Edad y validación
    edad = int(input('Ingrese su edad en número (debe ser mayor de 16 años): '))
    while edad < 16:
        edad = int(input('Edad inválida, ingrésela nuevamente: '))
    # Género y validación
    print("Género:\nA- Masculino\nB- Femenino\nC- Otro ")
    genero = (input('Ingrese la opción correspondiente a su género: ')).upper
    while genero!="A" or genero!="B" or genero!="C":
        genero = int(input('Opción inválida, reingrese la opción correspondiente a su género: '))
    # Entradas y validación
    print("Tipos de entrada disponibles:\nA- General\nB- Campo delantero\nC- Platea ")
    entrada = (input('Ingrese la opción correspondiente a la entrada que dese comprar: ')).upper
    while entrada!="A" or entrada!="B" or entrada!="C":
        entrada = int(input('Opción inválida, reingrese la opción correspondiente a la entrada que desea comprar: '))
    # Medios de pago y validación
    print("Medios de pago disponibles:\nA- Tarjeta de crédito\nB- Tarjeta de débito\nC- Efectivo ")
    medPago = (input('Ingrese la opción correspondiente a la forma de pago que desea utilizar: ')).upper
    while medPago!="A" or medPago!="B" or medPago!="C":
        entrada = int(input('Opción inválida, reingrese la opción correspondiente a la forma de pago que desea utilizar: '))

    # Subtotal según tipo de entrada y medio de pago
    match entrada:
        case "A":
            if medPago == "A":
                subtotal = general - general*0.2
                print("El precio a abonar es de: $" + str(subtotal))
            elif medPago == "B":
                subtotal = general - general*0.15
                print("El precio a abonar es de: $" + str(subtotal))
            else:
                print("El precio a abonar es de: $" + str(general))
        case "B":
            if medPago == "A":
                subtotal = campo - campo*0.2
                print("El precio a abonar es de: $" + str(subtotal))
            elif medPago == "B":
                subtotal = campo - campo*0.15
                print("El precio a abonar es de: $" + str(subtotal))
            else:
                print("El precio a abonar es de: $" + str(campo))
            
            

        case "C":
            if medPago == "A":
                subtotal = platea - platea*0.2
                print("El precio a abonar es de: $" + str(subtotal))
            elif medPago == "B":
                subtotal = platea - platea*0.15
                print("El precio a abonar es de: $" + str(subtotal))
            else:
                print("El precio a abonar es de: $" + str(platea))
    



