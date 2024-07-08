# Crear un programa que solicite al usuario que ingrese una letra. Se deberá
# validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas).

print("Ingrese una letra")
letra = str(input())

while letra != "U" and letra != "T" and letra != "N":
    print("Entrada no valida, vuelva a ingresar una letra")
    letra = str(input())

print("VALIDADA!")