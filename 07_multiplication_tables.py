"""
TABLAS DE MULTIPLICAR
Imprime todas la tablas de multiplicar del 1 al 10.
"""

for table_number in range(1, 11):
    print(f"tabla del {table_number}")
    for number in range(1, 11):
        print(f"{number} x {table_number} = {number * table_number}")
        print()