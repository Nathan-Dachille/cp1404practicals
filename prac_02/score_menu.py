"""Gets a valid score, prints a result and shows stars representing the score."""


def main():
    pass


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


main()
