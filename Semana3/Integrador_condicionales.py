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
print("Bienvenido a Ferrete Lámparas, donde lo único más bajo que el consumo es el precio.\n1- Argentinaluz\n2- FelipeLamparas\n3- Otra marca\n")
opcMarca = int(input('Ingrese la opción marca de lámparas de bajo consumo que desea comprar: '))

while validMarca == 0:
    if opcMarca > 3 or opcMarca < 0 or opcMarca != int:
     marca = int(input('La opción ingresada no es válida, ingrese la opción de marca de lamparas que desea comprar nuevamente: '))
    else:
        validMarca = 1

# Pedimos y validamos la cantidad   
cantidad = int(input('Ingrese la cantidad de lámparas de bajo consumo que desea comprar (en número): '))

while validCantidad == 0:
    if cantidad < 0 or cantidad != int:
     cantidad = int(input('La cantidad ingresada no es válida, ingrese la cantidad de lamparas que desea comprar nuevamente: '))
    else:
        validCantidad = 1


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
        if opcMarca == 1 or marca == 2:
            descuento = totalSinDesc*0.25
        else:
            descuento = totalSinDesc*0.2
    case 5:
        if marca == 1:
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
      print("Usted está comprando lámparas de la marca Argentinaluz\n")
    case 2:
      print("Usted está comprando lámparas de la marca FelipeLamparas\n")
    case 3:
      print("Usted está comprando lámparas de una marca diferente a Argentinaluz o FelipeLamparas\n")

print("La cantidad de lámparas a comprar es:", str(cantidad))

print("El total a pagar sin descuentos es:", str(totalSinDesc))


if descuento>0:
   prtDescuento = str(descuento)
   print("\nEl descuento obtenido por su compra es de:", prtDescuento)


if totalConDesc>4000:
   descuentoAdicional = totalConDesc*0.05
   totalConDesc = totalConDesc - descuentoAdicional
   print("Además, obtuvo un descuento adicional por compra superior a $4000 de:", str(descuentoAdicional))
   print("TOTAL A PAGAR CON DESCUENTO:", str(totalConDesc))
