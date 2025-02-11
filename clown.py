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

    def send_in_the_clown(self):
        """
        The clown is called onto the stage.
            
        He carries his act, and is placed in the _acts first.
        Then the show commences with the first act, and the remaining acts follow.
        """
        print("{}.".format(self.clown.split()[-1]))
        self._acts = [self.clown, self.circus[1]]
        self._call_character(self.clown)

    def _call_character(self, character: str) -> None:
        """
        The chracter's name is called.

        Args:
            character (str): the name of the character
        """
        punctuation = "!" if len(self._acts)+1 == self.max_acts else "."
        print(character[0].upper()+character[1:]+punctuation) if character != self.circus[-1] else None


clown = Clown()
clown.send_in_the_clown()