"""P1404 Seminar
Monster Class"""


class Monster:
    """Monster class"""

    def __init__(self, name="Mike", number_of_teeth=0, colour="blue"):
        """Represent a Monster."""
        self.name = name
        self.number_of_teeth = number_of_teeth
        self.colour = colour

    def __str__(self):
        """Returns the string version of Monster"""
        return f"{self.name}, {self.number_of_teeth}, {self.colour}"

    def __repr__(self):
        return f"({vars(self)})"

    def is_scary(self):
        """Determine if monster is scary by number of teeth or monster colour"""
        return self.number_of_teeth > 16 or self.colour == "red"
