""" 
Desafío:
- Ordena una lista de números de menor a mayor usando el algoritmo "ordenamiento de burbuja".
"""

def ordenamiento_burbuja(lista: list) -> list:
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplos:
print(ordenamiento_burbuja([5, 3, 6, 1, 9, 2])) # [1, 2, 3, 5, 6, 9]