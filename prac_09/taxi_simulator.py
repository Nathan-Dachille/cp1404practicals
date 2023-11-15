"""Taxi Simulator Prac."""
from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Gets a valid option from the menu and calls the required function."""
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill_to_date = drive_taxi(current_taxi, bill_to_date)
        elif choice == 'c':
            current_taxi = taxis[choose_taxi(taxis)]
        elif choice != 'q':
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def drive_taxi(current_taxi, bill_to_date):
    is_valid_input = False
    while not is_valid_input:
        try:
            distance = int(input("Drive how far? "))
            if 0 > distance:
                raise ValueError
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid distance.")
    current_taxi.start_fare()
    current_taxi.drive(distance)
    current_fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${current_fare:.2f}")
    return current_fare + bill_to_date


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
