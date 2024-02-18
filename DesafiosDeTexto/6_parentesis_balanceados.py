""" 
Desafío: 
Crea una función que revise una cadena de caracteres que solamente va a contener paréntesis, y 
determine si la cadena de caracteres está balanceada.
"""

def parentesis_balanceados(cadena: str) -> bool:
    pila = []
    for caracter in cadena:
        if caracter == "(":
            pila.append(caracter)
        elif caracter == ")":
            if len(pila) == 0:
                return False
            pila.pop()
    return len(pila) == 0

# Ejemplos:
print(parentesis_balanceados("()")) # True
print(parentesis_balanceados("(()")) # False
print(parentesis_balanceados("(()())")) # True