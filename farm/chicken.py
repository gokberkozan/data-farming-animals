"""Chicken animal."""
from farm.animal import Animal


class Chicken(Animal):
    """A chicken; only females lay eggs."""

    def __init__(self, gender):
        super().__init__()
        self.gender = gender
        self.eggs = 0

    def talk(self):
        """Return the sound the chicken makes, depending on its gender."""
        if self.gender == "male":
            return "cock-a-doodle-doo"
        return "cluck cluck"

    def feed(self):
        """Feed the chicken: gain energy, females also lay 2 eggs."""
        super().feed()
        if self.gender == "female":
            self.eggs += 2
