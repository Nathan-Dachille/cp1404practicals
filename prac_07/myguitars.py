"""myguitars.py generates Guitar objects for each guitar in guitars.csv, then sorts and displays."""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Reads CSV, generates Guitar objects and displays."""
    guitars = []

    with open(FILENAME, 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], int(row[1]), float(row[2]))
            guitars.append(guitar)

    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
