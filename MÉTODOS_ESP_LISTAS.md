# METODOS PARA LISTAS
Lista especiales para métodos vistos en clase

## Métodos de acceso

- **append**(elemento): Agrega elemento al final de la lista.
- **insert**(posicion,elemento): Agrega el elemento segun posición.
- **extend**(lista): Extiende la lista tipo left joint recibiendo otra lista como argumento.
- **remove**(elemento): Borra la primer coincidencia con el elemento que toma como argumento. Lo mismo hace la *keyword* **del** con su sintaxis ***del lista [index ó rango(a:b)]***.
- **pop**(index): Elimina el elemento que coincide en index con el argumento y devuelve el elemento. Default = ultimo de la lista.
- **clear**(): Limpia la lista.
- **index**(elemento,start=0,end=last): Devuelve el número de index del elemento que toma como argumento obligatorio. Además recibe como parámetros opcionales el inicio y fin del rango de busqueda.


## Métodos de ordenamiento

- **sort**(): Ordena los elementos de la lista en orden ascendente(numérico).
- **reverse**(): Invierte el orden de los elementos de la lista.


## Copia
Formas de copiar listas
### **shallow copy**: ***copy.copy(lista)***
Copia superficial. se copia la lista, pero sus elementos siguen siendo compartidos entre ambas y si alguno se modifica en una se modifica en todas.
### **deep copy**: ***copy.deepcopy(lista)***
Genera una copia independiente de la lista, duplicando sus elementos.

## Ciclos for
Funciones iterables específicas para listas
### enumerate()
``` python
frutas = ["a", "b"]
for indice, fruta in ***enumerate*** (frutas):
    print (f"Índice: {indice}, Fruta{fruta}")
```

### zip()
Itera multiples listas como si de una tabla se tratase
```python
nombres = ["a", "b"]
edades = [1, 2]
for nombre, edad in ***zip*** (nombres, edades):
    print (f"Nombre: {nombre}, Edad{edad}")
```

