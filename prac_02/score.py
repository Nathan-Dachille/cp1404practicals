"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Asks for a score and rates it."""
    score = int(input("Enter score: "))
    print(test_score(score))


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


main()
