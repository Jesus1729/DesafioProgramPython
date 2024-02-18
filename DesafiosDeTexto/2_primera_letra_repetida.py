""" 
Desafío:
- Crea una función que reciba una cadena de texto, con las siguientes características:
    - Retorne el primer caracter que aparezca en la cadena de texto más de una vez.
    - No podrá retornar un espacio vacío como el primer caracter repetido.
    - En caso de no haber caracteres repetidos, deberá retornar None.
"""

def primera_letra_repetida(palabra: str) -> str:
    palabra = palabra.lower()
    for letra in palabra:
        if palabra.count(letra) > 1 and letra != " ":
            return letra
    return None

# Ejemplos:

print(primera_letra_repetida("Hola")) # None
print(primera_letra_repetida("Hola, mundo")) # o