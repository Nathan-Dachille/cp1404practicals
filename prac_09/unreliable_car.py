"""
CP1404/CP5632 Practical
UnreliableCar class
"""
from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """Version of Car class with a reliability property."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise UnreliableCar object."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Chance to drive UnreliableCar depending on reliability property."""
        if uniform(0, 100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        else:
            distance = 0
        return distance
