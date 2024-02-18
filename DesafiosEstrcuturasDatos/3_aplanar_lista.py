""" 
Desafío:
- Crea una función que reciba una lista con elementos anidados y retorne una lista aplanada.
- Recibir una lista anidada de dos dimensiones
- Retornar una nueva lista de una sola dimensión
- Debe contener todos los elementos de la lista exterior y la lista aniada.
- En el mismo orden
"""

def aplanar_lista(lista):
    return [elemento for sublista in lista for elemento in (sublista if type(sublista) is list else [sublista])]

# Ejemplos:
print(aplanar_lista([2, 3, 4, [3, 2]]) ) # [2, 3, 4, 3, 2]
print(aplanar_lista([2, 3, 4, [[2]]])) # [2, 3, 4, [2]]