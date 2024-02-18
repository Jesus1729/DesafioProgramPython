""" 
Desafío:
- Crea una función que reciba un número que indique la cantidad de filas requeridas para el triángulo de Pascal.
- Debe retornar una lista anidada.
- Cada elemento va a ser una lista correspondiente a una fila del triángulo.
"""

def triangulo_pascal(filas: int) -> list:
    if filas == 0:
        return []
    elif filas == 1:
        return [[1]]
    else:
        triangulo = triangulo_pascal(filas - 1)
        nueva_fila = [1]
        fila_anterior = triangulo[-1]
        for i in range(len(fila_anterior) - 1):
            nueva_fila.append(fila_anterior[i] + fila_anterior[i + 1])
        nueva_fila += [1]
        triangulo.append(nueva_fila)
        return triangulo

# Ejemplo:
print(triangulo_pascal(4)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
