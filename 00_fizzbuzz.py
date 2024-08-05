"""
El famoso "FIZZ BUZZ"
Escribe un programa que muestre por consola
(con un print) los número de 1 a 100 (ambos incluidos y con un salto de linea entre cada impresión), sustituyendo los siguientes:

Múltiplos de 3 por la palabra "fizz".
Múltiplos de 5 por la palabra "buzz".
Múltiplos de 3 y de 5 a la ves por la palabra "fizzbuzz".
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number } FIZZBUZZ")
    elif number % 3 == 0:
        print(f"{number} FIZZ")
    elif number % 5 == 0:
        print(f"{number} buzz")
    else:
        print(number)