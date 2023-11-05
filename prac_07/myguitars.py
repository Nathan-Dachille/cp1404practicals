"""myguitars.py generates Guitar objects for each guitar in guitars.csv, then sorts and displays."""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Gets new guitar objects from user input."""
    guitars = read_guitars()

    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        is_valid_cost = False
        is_valid_year = False
        while not is_valid_year:
            try:
                year = int(input("Year: "))
                is_valid_year = True
            except ValueError:
                print("Invalid year!")
        while not is_valid_cost:
            try:
                cost = float(input("Cost: $"))
                is_valid_cost = True
            except ValueError:
                print("Invalid cost!")
        guitars.append(Guitar(name, year, cost))
        print(guitars[-1], "added.")
        name = input("Name: ")

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    write_guitars(guitars)


def write_guitars(guitars):
    """Write guitar object properties to csv.file."""
    with open(FILENAME, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            row = [guitar.name, guitar.year, guitar.cost]
            writer.writerow(row)


def read_guitars():
    """Reads CSV and returns list of Guitar objects."""
    guitars = []
    with open(FILENAME, 'r', newline='') as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            guitars.append(guitar)
    return guitars


if __name__ == '__main__':
    main()
