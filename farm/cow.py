"""Cow animal."""
from farm.animal import Animal


class Cow(Animal):
    """A cow."""

    def talk(self):
        """Return the sound a cow makes."""
        return "moo"
