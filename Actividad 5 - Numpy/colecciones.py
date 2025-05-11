import numpy

lista1 = ["hola", True, 1, "Json", 3]
#lista2 = np.array([1, 2, 3, 4, 5])

tupla1 = tuple(lista1)
conjunto1 = set(lista1)
diccionario1 = {"Nombre":"Carlos",
                "Edad": 45,
                "Casado": True,
                "Ocupación": "Streamer jodido",
                "Años laborando": 25,}

print(lista1)
print(tupla1)
print(conjunto1)
print(diccionario1)

#para añadirelementos a una lista #lista.append()
#para insertar un elemento en una posición de la lista #lista.insert(posición de la lista, agregación)
#para contar los valores de la lista #lista.count()
#para contar cuantos valores especificos hay de una lista #lista.count(elemento de la lista)
#para eliminar elementos repetidos de una lista, convertir la lista a set x = set(lista)