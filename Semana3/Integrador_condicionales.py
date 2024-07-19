#Ferrete Lámparas


# En una ferretería se quiere implementar un sistema que permita a los usuarios saber cuánto deberán pagar por la compra de lámparas de bajo consumo. Se tiene en cuenta que todas las lámparas cuestan $800.

# A partir de la cantidad y marca de las lámparas compradas (solo se puede comprar una marca por vez) se aplicará el siguiente descuento:

# Si compra 6 o más  lámparas bajo consumo tiene un descuento del 50%. 

# Si compra 5  lámparas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.

# Si compra 4  lámparas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.

# Si compra 3  lámparas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.

# Por otro lado, si el importe final con descuento suma más de $4000  se obtiene un descuento adicional de 5%.

#Mostrar por pantalla: 

#Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

# ________________________________________________________________________________________________________________________________________

# MARCAS POSIBLES:
# ArgentinaLuz
# FelipeLamparas
# otraMarca

# DESCUENTOS POSIBLES:
# llevando 6 o mas-------> todas las marcas:50%
# llevando 5-------------> Argentinaluz:40%, FelipeLamparas y otras:30%
# llevando 4-------------> Argentinaluz y FelipeLamparas:25%, otras
# llevando 3-------------> Argentinaluz:15%; FelipeLamparas:10%, otras:5%
# descuento adiciona-----> 5% sobre el precio con descuento si supera $4000

valorLamp = 800
validMarca = 0
validCantidad = 0

# Pedimos y validamos la marca
print("\nBienvenido a Ferrete Lámparas, donde lo único más bajo que el consumo es el precio.\nTodas nuestras lámparas son de bajo consumo y tienen el valor de $800.\n\nDESCUENTOS:\nLlevando 6 o más-------> todas las marcas:50%\n\nLlevando 5-------------> Argentinaluz:40%, FelipeLamparas y otras:30%\n\nLlevando 4-------------> Argentinaluz y FelipeLamparas:25%, otras\n\nLlevando 3-------------> Argentinaluz:15%, FelipeLamparas:10% y otras:5%\n\nDESCUENTO ADICIONAL----> 5% sobre el precio con descuento si supera $4000\n\nMARCAS DESTACADAS:\n1- Argentinaluz\n2- FelipeLamparas\n3- Otra marca\n")
opcMarca = int(input('Ingrese la opción marca de lámparas de bajo consumo que desea comprar: '))

while validMarca == 0:
    if opcMarca==3 or opcMarca==2 or opcMarca==1:
       validMarca = 1
    else:
       opcMarca = int(input('\nLa opción ingresada no es válida, ingrese la opción de marca de lamparas que desea comprar nuevamente: '))

# Pedimos y validamos la cantidad   
cantidad = int(input('\nIngrese la cantidad de lámparas de bajo consumo que desea comprar (en número): '))

while validCantidad == 0:
    if cantidad > 0 and cantidad < 100000 :
       validCantidad = 1
    else:
        cantidad = int(input('\nLa cantidad ingresada no es válida, ingrese la cantidad de lamparas que desea comprar nuevamente: '))


totalSinDesc = cantidad * valorLamp
descuento = 0

# Verificamos descuentos
if cantidad<6:
   match cantidad:
    case 3:
        if opcMarca == 1:
            descuento = totalSinDesc*0.15
        elif opcMarca == 2:
            descuento = totalSinDesc*0.10
        else:
            descuento = totalSinDesc*0.05
    case 4:
        if opcMarca == 1 or opcMarca == 2:
            descuento = totalSinDesc*0.25
        else:
            descuento = totalSinDesc*0.2
    case 5:
        if opcMarca == 1:
            descuento = totalSinDesc*0.4
        else:
            descuento = totalSinDesc*0.3
    case _:
        descuento = 0
else:
   descuento = totalSinDesc*0.5

# Obtenemos el total con descuento
totalConDesc = totalSinDesc-descuento

# Salida de consola
#Marca, cantidad de lámparas, total a pagar sin descuento, el descuento obtenido si corresponde, el descuento adicional (si corresponde) y el total a pagar con descuento.

match opcMarca:
    case 1:
      print("\nUsted está comprando lámparas de la marca Argentinaluz\n")
    case 2:
      print("\nUsted está comprando lámparas de la marca FelipeLamparas\n")
    case 3:
      print("\nUsted está comprando lámparas de una marca alternativa a Argentinaluz o FelipeLamparas\n")

print("La cantidad de lámparas en su carrito de compra es de: " + str(cantidad))




if descuento>0:
   totalSDR = str(round(totalSinDesc, 2))
   print("\nEl precio total de su compra sin descuentos es de: $" + totalSDR)
   DescuentoR = str(round(descuento, 2))
   print("\nEl descuento obtenido por su compra es de: $" + DescuentoR)


if totalConDesc>4000:
   descuentoAdicional = totalConDesc*0.05
   totalConDesc = totalConDesc - descuentoAdicional
   print("\nAdemás, obtuvo un descuento adicional por compra superior a $4000 de: $" + str(descuentoAdicional))

totalConDescR = str(round(totalConDesc, 2))
print("\n\nTOTAL A PAGAR: $" + totalConDescR + "\n")
