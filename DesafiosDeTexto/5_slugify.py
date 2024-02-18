""" 
Nota:
- Slug -> parte de una URL que utiliza palabras clave que permite que la URL sea legible.
- Un Slug contiene solo caracteres alfanuméricos y guiones como separador.
- Slugify -> Proceso de convertir un texto en un slug.
Desafío:
- Crea una función que reciba una cadena de texto y la convierta en un slug.
- Remover caracteres que no son alfanuméricos como: slashes, backslashes, asteriscos, signos de porcentaje, etc.
- Todos los espacios de la cadena de texto deben ser reemplazados por guiones.
- No usar librerías como python-slugify, solo es válido usar el módulo re.
"""
def slugify(cadena: str) -> str:
    import re
    return re.sub(r'[^a-zA-Z0-9]+', '-', cadena).lower()

# Ejemplos:
print(slugify("Hola, Mundo!")) # hola-mundo
print(slugify("texto% con carácteres* raros")) # texto-con-caracteres-raros
print(slugify("Texto con espacios")) # texto-con-espacios
print(slugify("Texto con / y \ y *")) # texto-con-y-y