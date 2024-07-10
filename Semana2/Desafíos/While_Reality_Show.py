# De los 3 Jugadores de un Reality Show, se registra:
# nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibió en la etapa de votos
# Informar:
# a. nombre del candidato con más votos
# b. nombre y edad del candidato con menos votos
# c. el promedio de edades de los candidatos
# d. total de votos emitidos.
# Todos los datos se ingresan mediante input()

# Input de datos

print("Ingrese el nombre del primer participante:")
nombre1 = str(input())
print("Ingrese la edad en número del primer participante (mayor de 25):")
edad1 = int(input())
print("Ingrese la cantidad de votos del primer participante (en número):")
votos1 = int(input())

print("Ingrese el nombre del segundo participante:")
nombre2 = str(input())
print("Ingrese la edad en número del segundo participante (mayor de 25):")
edad2 = int(input())
print("Ingrese la cantidad de votos del segundo participante (en número):")
votos2 = int(input())

print("Ingrese el nombre del tercer participante:")
nombre3 = str(input())
print("Ingrese la edad en número del tercer participante (mayor de 25):")
edad3 = int(input())
print("Ingrese la cantidad de votos del tercer participante (en número):")
votos3 = int(input())

# Comparación de votos

if votos2<votos1>votos3:
    masVotado = str("El candidato con más votos es " + nombre1)
elif votos1<votos2>votos3:
    masVotado = str("El candidato con más votos es " + nombre2)
elif votos1<votos3>votos2:
    masVotado = str("El candidato con más votos es " + nombre3)
else:
    masVotado = "No hay un ganador, ya que existe un empate de dos o más participantes."
    

if votos2>votos1<votos3:
    menosVotado = str("El candidato con menos votos es " + nombre1 + " y su edad es " + str(edad1) + " años")
elif votos1>votos2<votos3:
    menosVotado = str("El candidato con menos votos es " + nombre2 + " y su edad es " + str(edad2) + " años")
elif votos1>votos3<votos2:
    menosVotado = str("El candidato con menos votos es " + nombre3 + " y su edad es " + str(edad3) + " años")
else:
    menosVotado= "No hay un candidato menos votado, ya que dos o más comparten la cantidad mínima de votos."
    

# Promedios y sumatorias

totalVotos= votos1+votos2+votos3
promEdad = (edad1+edad2+edad3)/3

# Variable de control

control = 0

# Condicional

while control == 0 : 
    if votos1 >= 0 and votos2 >= 0 and votos3 >= 0:
        if edad1 > 25 and edad2 > 25 and edad3 > 25:
            control = 1
            print(masVotado)
            print(menosVotado)
            print("El total de votos emitidos es " + str(totalVotos))
            print("El promedio de edad de los candidatos es de " + str(promEdad) + " años")
        else:
            print("La edad de cada participante debe ser mayor a 25 años \nIngrese las edades nuevamente.")
            print("Ingrese la edad en número del primer participante (mayor de 25):")
            edad1 = int(input())
            print("Ingrese la edad en número del segundo participante (mayor de 25):")
            edad2 = int(input())
            print("Ingrese la edad en número del tercer participante (mayor de 25):")
            edad3 = int(input())
    else:
        print("La cantidad de votos de cada candidato debe ser mayor o igual que 0 \nIngrese las cantidades nuevamente.")
        print("Ingrese la cantidad de votos del primer participante (en número):")
        votos1 = int(input())
        print("Ingrese la cantidad de votos del segundo participante (en número):")
        votos2 = int(input())
        print("Ingrese la cantidad de votos del tercer participante (en número):")
        votos3 = int(input())