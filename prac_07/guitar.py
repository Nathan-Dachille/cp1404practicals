"""Prac06 Guitar class"""


class Guitar:
    """Represent information about guitars."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar object."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return information as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of Guitar object."""
        return 2023 - self.year

    def is_vintage(self):
        """Return boolean True is age is greater than or equal to 50 years."""
        return self.get_age() >= 50
