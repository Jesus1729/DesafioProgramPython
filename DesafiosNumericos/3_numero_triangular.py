""" 
Desafío:
- Crea una función que reciba el número de la fila del triángulo de puntos.
- Calcula el número correspondiente a esa fila.
"""

def numero_triangular(fila: int) -> int:
    return (fila * (fila + 1)) // 2

# Ejemplos:
print(numero_triangular(3)) # 6
print(numero_triangular(4)) # 10
print(numero_triangular(5)) # 15    
print(numero_triangular(6)) # 21