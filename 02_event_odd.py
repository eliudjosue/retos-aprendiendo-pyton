"""
POR O IMPAR
Crea un programa que compruebe si un número entero es par o impar
"""

try:
    number = int(input("Introduzca un número: "))
    if number % 2 == 0:
        print(f"El {number} es par")
    else:
        print(f"El {number} es impar")
except ValueError:
    print("Introdúzca un valor valido")