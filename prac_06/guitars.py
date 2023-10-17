"""Prac06 guitars.py
Estimated Time: 30min
Actual Time: 41min
"""

from prac_06.guitar import Guitar

print("My Guitars!")
name = input("Name: ")
guitars = []
while name != "":
    while True:
        try:
            year = int(input("Year: "))
            break
        except ValueError:
            print("Invalid year!")
    while True:
        try:
            cost = float(input("Cost: $"))
            break
        except ValueError:
            print("Invalid cost!")
    guitars.append(Guitar(name, year, cost))
    print(guitars[-1], "added.")
    name = input("Name: ")

for i, guitar in enumerate(guitars, 1):
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} "
          f"{'(vintage)' if guitar.is_vintage() else ''}")
