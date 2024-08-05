"""
CONTADOR DE VOCALES
Cree un programa que cuente cuantas vocales tiene una cadena de texto.
"""
vowels = "aeiou"
counter = 0
chars = ""

text = input("Introduce una cadena de texto: ")

for char in text.lower():
    if char in vowels:
        chars = f"{chars}{char}"
        counter += 1

print(f"Total de vocales: {counter} y las vocales son {chars}")