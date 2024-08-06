"""
INVERSIÓN DE CADENAS
Crea una funcion que invierta una cadenma de texto
"""

def reverse_string(text):
    reversed_string = ""
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string
    
print(reverse_string("paralelpipedo!"))