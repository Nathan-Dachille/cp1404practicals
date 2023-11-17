"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Special case of the Taxi class with a fanciness property that scales price_per_km."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Car but with current fare distance and flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall
