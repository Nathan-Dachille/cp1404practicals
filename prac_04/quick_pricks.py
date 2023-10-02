"""Generates a set number of quick picks and prints."""
from random import randint


def main():
    """Ask for number of quick picks, generate and then print."""
    number_of_quick_picks = int(input("How many quick picks? "))
    quick_picks = generate_quick_picks(number_of_quick_picks)
    print_quick_picks(quick_picks)


def generate_quick_picks(number_of_quick_picks):
    """Generates quick picks."""
    quick_picks = []
    for i in range(number_of_quick_picks):
        quick_pick = []
        for j in range(6):
            quick_pick.append(randint(1, 45))
        quick_picks.append(quick_pick)
    return quick_picks


def print_quick_picks(quick_picks):
    """Prints quick picks."""
    for quick_pick in quick_picks:
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_pick))


main()
