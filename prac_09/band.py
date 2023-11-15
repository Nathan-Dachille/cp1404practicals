"""Band class for CP1404"""


class Band:
    """Band class."""
    def __init__(self, name):
        """Initialise Band class"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def play(self):
        """Return a list of strings showing the musicians in a band playing their first (or no) instrument."""
        playing = ''
        for musician in self.musicians:
            playing = playing + musician.play() + '\n'
        return playing
