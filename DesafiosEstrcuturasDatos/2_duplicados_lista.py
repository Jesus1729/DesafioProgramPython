""" 
Desafío:
- Crea una función que permita identificar los elementos duplicados en una lista.
- La función debe retornar una lista con los elementos duplicados.
- En caso de que no haya elementos duplicados, debe retornar una lista vacía.
"""

def ecnontrar_duplicados(lista: list) -> list:
    duplicados = []
    for i in lista:
        if lista.count(i) > 1 and i not in duplicados:
            duplicados.append(i)
    return duplicados

# Ejemplos:
print(ecnontrar_duplicados([1, 2, 3, 4, 5, 6])) # []
print(ecnontrar_duplicados(["ana", "paco", "juan", "ana", "paco", "luis"])) # ["ana", "paco"]