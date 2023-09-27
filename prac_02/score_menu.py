"""Gets a valid score, prints a result and shows stars representing the score."""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Ask user for choice from MENU, then execute required function."""
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(test_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def test_score(score: int) -> str:
    """Tests a score between 0 and 100 and returns a result."""
    if score < 0:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    elif score <= 100:
        result = "Excellent"
    else:
        result = "Invalid score"
    return result


def show_stars(stars):
    """Prints stars number of stars."""
    print(stars * "*")


def get_score():
    """Gets a score between 0 and 100."""
    score = int(input("Please enter a score between 0 and 100: "))
    while (score > 100) or (score < 0):
        print(f"{score} is an invalid score.")
        score = int(input("Please enter a score between 0 and 100: "))
    return score


main()
