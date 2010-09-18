"""Composer takes musical notions and converts them to midi sounds.
"""

class Composer(object):
    """Converts musical stroke to sound."""

    def __init__(self, color, mood):
        self.color = color
        self.mood = mood
        self.key = (0, 2, 4, 5, 7, 9, 11)



