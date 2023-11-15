"""Taxi Simulator Prac."""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Gets a valid option from the menu and calls the required function."""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            pass
        elif choice == 'c':
            current_taxi = taxis[choose_taxi(taxis)]
        elif choice != 'q':
            print("Invalid option.")
        print(MENU)
        choice = input(">>> ").lower()


def choose_taxi(taxis):
    """Returns a valid index for a taxi in taxis list."""
    is_valid_input = False
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")
    while not is_valid_input:
        try:
            taxi_index = int(input("Choose taxi: "))
            if 0 > taxi_index or taxi_index >= len(taxis):
                raise ValueError
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid taxi choice")
    return taxi_index


main()
