print("Ingrese un número")
numero = int(input())

while numero>9 or numero<=0:
    print ("Condición no cumplida, ingrese un número nuevamente")
    numero = int(input())
print("Condición cumplida!")