"""
Desafío:
- Crea una función para identificar si una palabra es un palíndromo, con las siguientes características:
    - Debe recibir una cadena de texto como parámetro.
    - Debe retornar True si la palabra es un palíndromo, False en caso contrario.
    - Las mayúsculas y minúsculas no deben importar.

"""

def es_palindromo(palabra: str) -> bool:
    palabra = palabra.lower()
    palabra = palabra.replace(" ", "")
    return palabra == palabra[::-1]

# Ejemplos:

print(es_palindromo("lapiz")) # False
print(es_palindromo("Anita lava la tina")) # True
print(es_palindromo("Hola")) # False
print(es_palindromo("reconocer")) # True