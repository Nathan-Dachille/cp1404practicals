"""Taxi Simulator Prac."""

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            pass
        elif choice == 'c':
            pass
        elif choice != 'q':
            print("Invalid option.")
        choice = input(">>> ").lower()


main()
