"""
CONVERSOR DE TEMPERATURAS
Crea un conversor entre grados Celsius y Fahrenheit.
"""

print("Conversor de temperatura:")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Celsius a Kelvin")
print("4. Kelvin a Celsius")

Choice = input("Elige una opcion: ")
degrees = float(input("Temperatura: "))

if Choice == "1":
    fahrenheit = (degrees * 9/5) + 32
    print(f"{degrees}°C son {fahrenheit}°F.")
elif Choice == "2":
    celsius = (degrees - 32 ) * 5/9
    print(f"{degrees}°F son {celsius}°C.")
elif Choice == "3":
    kelvin = degrees + 273
    print(f"{degrees}°C son {kelvin}°K.")
elif Choice == "4":
    celsius = degrees - 273
    print(f"{degrees}°K son {celsius}°C.")
else:
    print("Opción no valida.")