"""  
Desafío:
- Crea una función que reciba un número entero positivo y retorne el factorial de ese número, usando
un ciclo o una función recursiva.
"""

def factorial(numero: int) -> int:
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)
    
# Ejemplos:
print(factorial(5)) # 120
print(factorial(3)) # 6
print(factorial(6)) # 720
print(factorial(0)) # 1