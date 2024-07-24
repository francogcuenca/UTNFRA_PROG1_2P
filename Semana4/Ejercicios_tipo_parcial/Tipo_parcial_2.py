
# En el ingreso a un viaje en crucero nos solicitan
# nombre ,
# edad(mayores de 18),
# sexo("f" o "m") y
# estado civil("soltero", "casado" o "viudo");
# Se debe Informar al usuario lo siguiente:
# a)El nombre del hombre casado más joven.
# b)El sexo y nombre del pasajero/a más viejo.
# c)La cantidad de mujeres que hay casadas o viudas.
# d)El promedio de edad entre las mujeres.
# e)El promedio de edad entre los hombres solteros.

# Constantes y flags
EDAD_MIN = 18
flag_control = True
flag_comparacion = True

# Variables
# a) Hombre casado más joven
edad_casado_mas_joven = None
nombre_casado_mas_joven = None
# b) Pasajero más viejo
nombre_pasajero_mas_viejo = None
sexo_pasajero_mas_viejo = None
edad_pasajero_mas_viejo = None
# c) Cantidad de mujeres casadas o viudas
cant_casadas_viudas = 0
# d) Promedio de edad en mujeres
cant_mujeres = 0
acum_edad_mujeres = 0
prom_edad_mujeres = None
# e) Promedio de edad en hombres solteros
cant_hombres_solteros = 0
acum_edad_hombres_solteros = 0
prom_edad_hombres_solteros = None


while flag_control == True:
    # Ingreso de datos y validaciones
    nombre = input('\nIngrese el nombre del pasajero: ')
    edad = int(input('\nIngrese la edad del pasajero en número (debe ser mayor a 18): '))
    while not(edad > EDAD_MIN):
        edad = int(input('¡¡ERROR!! Edad inválida, reingrese la edad del pasajero en número (debe ser mayor a 18): '))
    sexo = (input('\nIngrese si el sexo del pasajero es femenino o masculino por su inicial ("F" o "M"): ')).upper()
    while not(sexo == "F" or sexo == "M"):
        sexo = (input('¡¡ERROR!! Opción no válida, reingrese el sexo del pasajero ("F" o "M"): ')).upper()
    estado_civil = (input('\nIngrese el estado civil del pasajero ("soltero", "casado" o "viudo"): ')).upper()
    while not(estado_civil == "SOLTERO" or estado_civil == "CASADO" or estado_civil == "VIUDO"):
        estado_civil = (input('¡¡ERROR!! Opción no válida, reingrese el estado civil del pasajero ("soltero", "casado" o "viudo"): ')).upper()
    continuar = (input('\nDesea seguir ingresando pasajeros (si/no): ')).upper()
    while not(continuar == "SI" or continuar == "NO"):
        continuar = (input('¡¡ERROR!! Opción inválida, indique si desea seguir ingresando pasajeros (si/no): ')).upper()
    if continuar == "NO":
        flag_control = False
    
    # Pasajero más viejo
    match flag_comparacion:
        case True:
            nombre_pasajero_mas_viejo = nombre
            sexo_pasajero_mas_viejo = sexo
            edad_pasajero_mas_viejo = edad
            flag_comparacion = False
        case _:
            if edad_pasajero_mas_viejo<edad:
                nombre_pasajero_mas_viejo = nombre
                sexo_pasajero_mas_viejo = sexo
                edad_pasajero_mas_viejo = edad
    
    # Casos solicitados
    match sexo:
        case "M":
            match estado_civil:
                case "SOLTERO":
                    cant_hombres_solteros += 1
                    acum_edad_hombres_solteros = acum_edad_hombres_solteros + edad
                    prom_edad_hombres_solteros = acum_edad_hombres_solteros/cant_hombres_solteros
                case "CASADO":
                    if edad_casado_mas_joven == None or edad_casado_mas_joven>edad:
                        edad_casado_mas_joven = edad
                        nombre_casado_mas_joven = nombre
        case "F":
            cant_mujeres += 1
            acum_edad_mujeres = acum_edad_mujeres + edad
            prom_edad_mujeres = acum_edad_mujeres/cant_mujeres
        
            match estado_civil:
                case "CASADO":
                    cant_casadas_viudas += 1
                case "VIUDO":
                    cant_casadas_viudas += 1

# Informe
# Se debe Informar al usuario lo siguiente:
# a)El nombre del hombre casado más joven.
# b)El sexo y nombre del pasajero/a más viejo.
# c)La cantidad de mujeres que hay casadas o viudas.
# d)El promedio de edad entre las mujeres.
# e)El promedio de edad entre los hombres solteros.

if not(nombre_casado_mas_joven == None):
    print('\nEl nombre del hombre casado más joven es',nombre_casado_mas_joven)

match sexo_pasajero_mas_viejo:
    case "M":
        sexo_pasajero_mas_viejo_print = "masculino"
    case "F":
        sexo_pasajero_mas_viejo_print = "femenino"

print('\nEl nombre del pasajero más viejo es',nombre_pasajero_mas_viejo,'y su sexo es',sexo_pasajero_mas_viejo_print)

if cant_casadas_viudas>0:
    print('\nHay un total de',cant_casadas_viudas,'mujeres casadas o viudas')

if cant_mujeres>0:
    print('\nEl promedio de edad entre las mujeres es',str(round(prom_edad_mujeres, 1)),'años.')

if cant_hombres_solteros>0:
    print('\nEl promedio de edad entre los hombres solteros es',str(round(prom_edad_hombres_solteros, 1)),'años.')
