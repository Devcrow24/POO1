#para añadirelementos a una lista #lista.append()
#para insertar un elemento en una posición de la lista #lista.insert(posición de la lista, agregación)
#para contar los valores de la lista #lista.count()
#para contar cuantos valores especificos hay de una lista #lista.count(elemento de la lista)
#para eliminar elementos repetidos de una lista, convertir la lista a set x = set(lista)

import numpy as np

lista1 = ["hola", True, 1, "Json", 3]
lista2 = np.array([1, 2, 3, 4, 5])

tupla1 = tuple(lista1)
#numpy
tupla2 = tuple(lista2)

conjunto1 = set(lista1)
#numpy
conjunto2 = set(lista2)

diccionario1 = {"Nombre":"Abdiel",
                "Edad": 18,
                "Casado": False,
                "Ocupación": "Estudiante",
                "Años laburando": 0,}
#numpy
claves = np.array(['valor1', 'valor2', 'valor3'])
valores = np.array([1,2,3])
diccionario2 = dict(zip(claves, valores))

#---------------------------------------Iniciating programing

print(lista1)
print(lista2)
print(tupla1)
print(tupla2)
print(conjunto1)
print(conjunto2)
print(diccionario1)
print(diccionario2)