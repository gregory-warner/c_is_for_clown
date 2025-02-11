class Clown:
    """
    C is for Clown

    This program prints the book: C is for Clown - A Circus of "C" Words.

    Attributes:
        circus   (list[str])    A list of circus characters.
        clown    (str)          Clown. Clarence Clown.
        max_acts (int)          The maximum number of carried characters.
        _acts    (list[str])    A list of carried characters.
    """

    def __init__(self):
        """Initialize the instance attributes"""
        self.circus: list[str] = [
            "Clarence Clown",
            "cats carrying canes",
            "collies carrying clubs",
            "cows carrying cakes and candles",
            "Caroline Catfish",
            "Clara Canary"
        ]

        self.clown: str = self.circus[0]
        self.max_acts: int = len(self.circus)-1
        self._acts: list[str] = []


clown = Clown()