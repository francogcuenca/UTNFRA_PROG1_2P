# Crear un programa que al ingresar un número puede calcular si es mayor,
# niño/a(menor de 10) o pre-adolescente (edad entre 10 y 13 años)
# adolescente (edad entre 13 y 17 años) de edad.

print("Ingrese su edad en número")
edad = int(input())

match edad:
    case edad if 0<=edad <= 10:
        print("Es menor")
    case edad if 10<edad<=13:
        print("Es pre-adolescente")
    case edad if 13<edad<=17:
        print("Es adolescente")
    case edad if edad>17:
        print("Es mayor")
    case _:
        print("Ingrese una edad válida")