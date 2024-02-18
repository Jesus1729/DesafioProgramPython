""" 
Desafío: Crea una función que determine si dos palabras son anagramas.
- No debe haber distinción entre mayúsculas y minúsculas.
"""

def anagramas(palabra1: str, palabra2: str) -> bool:
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplos:
print(anagramas("roma", "amor")) # True
print(anagramas("hola", "aloh")) # True
print(anagramas("hola", "alo")) # False
print(anagramas("cama", "casa")) # False