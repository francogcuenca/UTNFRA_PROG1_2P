'''
En un gimnasio se necesita un programa que permita ingresar datos de 20 socios Por cada socio, se
ingresa:
• Nombre completo.
• Tarifa Base (10000, no se podrá ingresar otro valor)
• Altura (en centímetros, mayor a 100 y menor a 250).
• Peso (en kilogramos, mayor a 30 y menor a 200).
• Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o
"Funcional".

Una vez ingresados todos los datos, el programa debe calcular e informar lo siguiente (informar por
print):
Los socios que realicen:
● Musculación, tendrán un incremento del 10%.
● Cardio, tendrán incremento del 10%.
● Funcional, un descuento del 10%

A. Por el número de DNI del alumno:
1. Terminados en 0 o 1:
● Informar la cantidad total de socios que realizan “Musculación” y su altura es
superior a “165”.

● El promedio total recaudado de los socios que realizan “Cardio” y su altura es
superior a “110”.
● El nombre y la altura del socio que realiza “Funcional” de menor peso.
2. Terminados en 2 o 3:
● Informar la cantidad total de socios que realizan “Cardio” y su altura es superior
a “165”.
● El promedio total recaudado de los socios que realizan “Funcional” y su altura es
superior a “110”.
● El nombre y la altura del socio que realiza “Musculación” de menor peso.
3. Terminados en 4 o 5:
● Informar la cantidad total de socios que realizan “Funcional” y su altura es
superior a “165”.
● El promedio total recaudado de los socios que realizan “Musculación” y su altura
es superior a “110”.
● El nombre y la altura del socio que realiza “Cardio” de menor peso.
4. Terminados en 6 o 7:
● Informar la cantidad total de socios que realizan “Musculación” y su altura es
inferior a “165”.
● El promedio total recaudado de los socios que realizan “Cardio” y su peso es
superior a “80”.
● El nombre y la altura del socio que realiza “Funcional” de mayor peso.
5. Terminados en 8 o 9:
● Informar la cantidad total de socios que realizan “Funcional” y su altura es
inferior a “165”.
● El promedio total recaudado de los socios que realizan “Musculación” y su peso
es superior a “120”.
● El nombre y la altura del socio que realiza “Musculación” de mayor peso.

B. Informar cuál fue el tipo de rutina de entrenamiento más elegida.
C. Los porcentajes de cada tipo de rutina de entrenamiento. Ejemplo: [30% Cardio, 40%
Funcional, 30% Musculación]
'''


'''
• Nombre completo.
• Tarifa Base (10000, no se podrá ingresar otro valor)
• Altura (en centímetros, mayor a 100 y menor a 250).
• Peso (en kilogramos, mayor a 30 y menor a 200).
• Rutina de entrenamiento: Debe elegir entre las opciones "Cardio", "Musculación" o
"Funcional".
'''
# Flag socios
flag_socios = 0

# Constantes
TARIFA_BASE = 10000
MAX_CANT_SOCIOS = 20
TARIFA_DESC = TARIFA_BASE - TARIFA_BASE * 0.1
TARIFA_INCR = TARIFA_BASE + TARIFA_BASE * 0.1
PESO_MAX= 200
PESO_MIN = 30
ALTURA_MAX = 250
ALTURA_MIN = 100
CARDIO = "CARDIO"
MUSCULACION = "MUSCULACION"
FUNCIONAL ="FUNCIONAL"

# Contadores
cont_musc_altura = 0

# Acumuladores
acum_cardio_recaudado = 0
menos_peso_funcional = None
menos_peso_funcional_nombre = None
menos_peso_funcional_altura = None

print('BIENVENIDO AL PROGRAMA DE INGRESO DE SOCIOS DEL GIMNASIO\nIngrese los datos de 20 socios:')

while flag_socios<MAX_CANT_SOCIOS:
    # Input y validación
    nombre = input('\nIngrese el nombre del socio: ')

    altura = int(input('\nIngrese la altura del socio en cm (mayor a 100 y menor a 250): '))
    while not(altura>ALTURA_MIN and altura<ALTURA_MAX):
        altura = int(input('¡¡ERROR!! Altura inválida, reingrese la altura del socio en cm (mayor a 100 y menor a 250): '))

    peso = int(input('\nIngrese el peso del socio en Kg (mayor a 30 y menor a 200): '))
    while not(peso>PESO_MIN and peso<PESO_MAX):
        peso = int(input('¡¡ERROR!! Peso inválido, reingrese el peso del socio en Kg (mayor a 30 y menor a 200): '))

    rutina = (input(f'\nTipos de rutina disponibles: \n{CARDIO}\n{MUSCULACION}\n{FUNCIONAL}\nIngrese el tipo de rutina del socio: ')).upper()
    while not(rutina==CARDIO or rutina==MUSCULACION or rutina==FUNCIONAL):
        rutina = (input(f'¡¡ERROR!!Tipo de rutina inválido, reingrese el tipo de rutina que realiza el socio: ')).upper()

    match rutina:
        case "CARDIO":
            print(f'\nLa tarifa de este socio es de ${TARIFA_INCR}, con un 10% de incremento sobre la tarifa base por tipo de rutina.')
            if altura>110:
                acum_cardio_recaudado += TARIFA_INCR 

        case "MUSCULACION":
            print(f'\nLa tarifa de este socio es de ${TARIFA_INCR}, con un 10% de incremento sobre la tarifa base por tipo de rutina.')
            if altura>165:
                cont_musc_altura += 1 

        case "FUNCIONAL":
            print(f'\nLa tarifa de este socio es de ${TARIFA_DESC}, con un 10% de descuento sobre la tarifa base por tipo de rutina.')
            if menos_peso_funcional == None or menos_peso_funcional>peso:
                menos_peso_funcional = peso
                menos_peso_funcional_nombre = nombre
                menos_peso_funcional_altura = altura
    # Incremento en la flag principal
    flag_socios += 1

print('\nINFORME DE SOCIOS INGRESADOS')
if cont_musc_altura>0:
    print(f'\nLa cantidad total de socios que realizan musculación y su altura es mayor a 165 cm es de {cont_musc_altura}.')
if acum_cardio_recaudado>0:
    print(f'\nEl promedio total recaudado de los socios que realizan cardio y su altura es mayor a 110 cm es de {acum_cardio_recaudado}.')
if menos_peso_funcional!=None:
    print(f'\nEl socio de menor peso que realiza funcional es {menos_peso_funcional_nombre} y su altura es de {menos_peso_funcional_altura} cm.')












    




