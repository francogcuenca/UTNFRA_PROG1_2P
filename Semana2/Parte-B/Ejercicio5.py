# Crear un programa que solicite 5 números mediante prompt. Calcular la
# suma acumulada y el promedio de los números ingresados.
valores = []
sumaAcumulada = 0

print("Ingrese el primer número:")
numero1 = int(input())
valores.append(numero1)
print("Ingrese el segundo número:")
numero2 = int(input())
valores.append(numero2)
print("Ingrese el tercer número:")
numero3 = int(input())
valores.append(numero3)
print("Ingrese el cuarto número:")
numero4 = int(input())
valores.append(numero4)
print("Ingrese el quinto número:")
numero5 = int(input())
valores.append(numero5)

for n in valores:
    sumaAcumulada += n
print("suma acumulada: " + str(sumaAcumulada))
print("Promedio: " + str(sumaAcumulada/5))