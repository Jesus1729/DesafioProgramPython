""" 
Desafío:
- Crea una función que eciba una cadena de texto que contenga la hora en formato de 12 horas (Horas:Minutos AM/PM), 
con las siguientes características:
    - Retorna la hora en formato de 24 horas.
"""

def conversion_formato_horario(hora: str) -> str:
    if hora[-2:] in ["am", "AM"]:
        if hora[:2] == "12":
            return "00" + hora[2:-2]
        else:
            return hora[:-2]
    else:
        if hora[:2] == "12":
            return hora[:-2]
        else:
            return str(int(hora[:2]) + 12) + hora[2:-2]

# Ejemplos:
print(conversion_formato_horario("12:00 am")) # 00:00
print(conversion_formato_horario("04:59 PM")) # 16:59