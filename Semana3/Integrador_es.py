# La juguetería El MUNDO DE CHARLY nos encarga un programa para conocer qué cantidad de materiales se necesita para la fabricación de distintos juguetes.

# CONFECCIÓN DE UN COMETA: 

#        B
#        ^
#   D /__|__\ C
#     \  |  /
#      \ | /
#       \|/
#        A

# Medidas:

#AB = Diágonal mayor

#DC = Diágonal menor

#BD y BC = lados menores

#AD y AC = lados mayores

#El usuario ingresará las medidas  BC, CD y DA.

#Detalles de construcción

#Debemos tener en cuenta que la estructura del cometa estará dada por un perímetro de varillas de plástico y los correspondientes entrecruces (DC y AB) del mismo material para mantener la forma del cometa.

#El cometa estará construido con papel de alta resistencia. La cola del mismo se construirá con el mismo papel que el cuerpo y representará un 10% adicional del necesario para el cuerpo.

#Necesitamos saber cuántos Mts de varillas de plástico y cuántos de papel son necesarios para la construcción en masa de 10 cometas. Tener en cuenta que los valores de entrada están expresados en Cms.

print("Ingrese las medidas solicitadas teniendo en cuenta que un cometa es básicamente un rombo y para serlo")
print("la medida de los lados menores debe ser más chica que la de los lados mayores. A su vez, la medida de")
print("la diagonal menor (DC) no puede ser más grande que la suma de la medida de los dos lados menores(DB y BC).\n")
print("CONFECCIÓN DE UN COMETA\n")
print("           B")
print("           .")
print("        .  |  .")
print("     D .___0___. C")
print("        .  |  .")
print("         . | .")
print("          .|.")
print("           .")
print("           A\n")

diagonalMenor = float(input('Ingrese la medida del cruce DC (diagonal menor)\ndel cometa en centímetros: '))
ladoMenor = float(input('Ingrese la medida del lado BC (lado menor)\ndel cometa en centímetros: '))
ladoMayor = float(input('Ingrese la medida del lado DA (lado mayor)\ndel cometa en centímetros: '))

control =  0
maxDM = ladoMenor*2
while control == 0:
    # Condición para que sea un rombo:
    # Lado mayor debe ser más largo que lado menor y la diagonal menor
    # tiene que ser más chica que la suma de ambos lados menores.
    # Todos los lados deben ser mayores a cero.    
    if ladoMayor<=ladoMenor and ladoMenor>0:
        print("La medida del lado mayor DA no puede ser menor a la del lado menor BC.")
        ladoMayor = float(input("Reingrese la medida del lado mayor en centímetros: "))
    elif ladoMenor<=0:
        print("La medida ingresada del lado menor BC no puede ser 0 o negativo.")
        ladoMenor = float(input("Reingrese la medida del lado menor en centímetros: "))
    elif diagonalMenor<=0 or diagonalMenor>maxDM:
        print("La medida ingresada de la diagonal menor DC no puede ser mayor a la suma de los lados menores.")
        print("Tampoco puede ser menor o igual a 0.")
        diagonalMenor =float(input("Reingrese la medida de la diagonal menor en centímeros: "))
    else:
        control = 1


# Pitágoras
# Habría que calcular la diagonal mayor del rombo:
# A0 + 0B del esquema
# Trabajaré directamente en metros
DC = diagonalMenor/100
BC = ladoMenor/100
DA = ladoMayor/100
# Tomando el triángulo DA A0 0D se calcula A0

D0 = DC/2
A0 = pow((pow(DA,2) -pow(D0, 2)),1/2)

# Tomando el triángulo D0 B0 BD se calcula B0
BD = BC
B0 = pow((pow(BD,2) -pow(D0, 2)),1/2)

# Hayando diagonal mayor
AB = B0+A0

totalVarilla = str(round((BC*2+DA*2+DC+AB)*10, 2))

totalPapel = str(round(((DC*AB)/2)*10*1.1), 2)

print("Teniendo en cuenta que se producirán 10 unidades del cometa confeccionado por usted,")
print("el total de varilla a utilizar es",totalVarilla,"metros lineales.\nY el total de papel es", totalPapel, "metros cuadrados")
