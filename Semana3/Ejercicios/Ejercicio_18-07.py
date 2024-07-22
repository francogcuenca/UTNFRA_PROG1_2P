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

#_____________________________________________________________________________________________________________________________

# Constantes
general = 16000
campo = 25000
platea = 30000

# Variables
ctrlCompra = 0
campoMasculino = 0
campoFemenino = 0
campoOtro = 0
contGenCred = 0
contEdadGenCred = 0


while ctrlCompra == 0:
    nombre = input('Ingrese su nombre completo: ')
    # Edad y validación
    edad = int(input('Ingrese su edad en número (debe ser mayor de 16 años): '))
    while edad < 16:
        edad = int(input('Edad inválida, ingrésela nuevamente: '))
    # Género y validación
    print("Género:\nA- Masculino\nB- Femenino\nC- Otro ")
    genero = (input('Ingrese la opción correspondiente a su género: ')).upper()
    while genero!= 'A' and genero!='B' and genero!='C':
        genero = (input('Opción inválida, reingrese la opción correspondiente a su género: ')).upper()
    # Entradas y validación
    print("Tipos de entrada disponibles:\nA- General\nB- Campo delantero\nC- Platea ")
    entrada = (input('Ingrese la opción correspondiente a la entrada que dese comprar: ')).upper()
    while entrada!="A" and entrada!="B" and entrada!="C":
        entrada = int(input('Opción inválida, reingrese la opción correspondiente a la entrada que desea comprar: '))
    # Medios de pago y validación
    print("Medios de pago disponibles:\nA- Tarjeta de crédito\nB- Tarjeta de débito\nC- Efectivo ")
    medPago = (input('Ingrese la opción correspondiente a la forma de pago que desea utilizar: ')).upper()
    while medPago!="A" and medPago!="B" and medPago!="C":
        entrada = (input('Opción inválida, reingrese la opción correspondiente a la forma de pago que desea utilizar: ')).upper()

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
            contGenCred += 1
            contEdadGenCred = contEdadGenCred + edad
        case "B":
            if medPago == "A":
                subtotal = campo - campo*0.2
                print("El precio a abonar es de: $" + str(subtotal))
            elif medPago == "B":
                subtotal = campo - campo*0.15
                print("El precio a abonar es de: $" + str(subtotal))
            else:
                print("El precio a abonar es de: $" + str(campo))
            match genero:
                case "A":
                    campoMasculino += 1
                case "B":
                    campoFemenino += 1
                case _:
                    campoOtro += 1
        case "C":
            if medPago == "A":
                subtotal = platea - platea*0.2
                print("El precio a abonar es de: $" + str(subtotal))
            elif medPago == "B":
                subtotal = platea - platea*0.15
                print("El precio a abonar es de: $" + str(subtotal))
            else:
                print("El precio a abonar es de: $" + str(platea))
    continuar = (input('¿Desea seguir comprando entradas? si/no: ')).upper()
    match continuar:
        case "SI":
            ctrlCompra = 0
        case "NO":
            ctrlCompra =1
        case _:
            ctrlCompra =1
if campoMasculino > 0 and campoMasculino > campoFemenino and campoMasculino > campoOtro:
    print("El género que más compro entradas de campo es el masculino")
elif campoFemenino >0 and campoFemenino>campoMasculino and campoFemenino>campoOtro:
    print("El género que más compro entradas de campo es el femenino")
elif campoOtro>0 and campoOtro>campoFemenino and campoOtro>campoMasculino:
    print("El género que más compro entradas de campo es un género no binario")
    
if contGenCred>0:
    promEdad = contEdadGenCred/contGenCred
    print(str(contGenCred),"personas compraron entradas de tipo General pagando con tarjeta de crédito y su edad promedio es",str(round(promEdad, 2))) 