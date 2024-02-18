""" 
Nota:
- Un número primo es un número natural mayor a 1 que solo es divisible por 1 y por sí mismo.
Desafío:
- Crea una función que reciba un número entero positivo y retorne True si es un número primo, False en caso contrario.
"""

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

# Ejemplos:
print(es_primo(3)) # True
print(es_primo(12)) # False
print(es_primo(43)) # True