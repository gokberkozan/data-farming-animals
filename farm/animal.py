# pylint: disable=too-few-public-methods
"""Parent class for all farm animals."""


class Animal:
    """A generic farm animal."""

    def __init__(self):
        self.energy = 0

    def feed(self):
        """Feed the animal, adding 1 energy."""
        self.energy += 1
