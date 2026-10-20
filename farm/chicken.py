"""Chicken animal."""
from farm.animal import Animal


class Chicken(Animal):
    """A chicken with a gender."""

    def __init__(self, gender):
        super().__init__()
        self.gender = gender

    def talk(self):
        """Return the sound the chicken makes, depending on its gender."""
        if self.gender == "male":
            return "cock-a-doodle-doo"
        return "cluck cluck"
