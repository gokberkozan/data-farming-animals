"""Cow animal."""
from farm.animal import Animal


class Cow(Animal):
    """A cow that produces milk."""

    def __init__(self):
        super().__init__()
        self.milk = 0

    def talk(self):
        """Return the sound a cow makes."""
        return "moo"

    def feed(self):
        """Feed the cow: gain energy and produce 2 liters of milk."""
        super().feed()
        self.milk += 2
