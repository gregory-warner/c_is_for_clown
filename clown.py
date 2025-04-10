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
        self._commence()
        self._continue_show()

    def _call_character(self, character: str) -> None:
        """
        The chracter's name is called.

        Args:
            character (str): the name of the character
        """
        punctuation = "!" if len(self._acts)+1 == self.max_acts else "."
        print(character[0].upper()+character[1:]+punctuation) if character != self.circus[-1] else None

    def _commence(self):
        """The act with the cat. The charcter is called and caught."""
        self._call_character(self._acts[-1])
        self._consider_to_carry()
        self._catch_character(self._acts[-1])

    def _consider_to_carry(self) -> None:
        """"
        Prints a question about Clarence carrying the current acts.
        Clarence considers to carry the current characters.
        """
        count = len(self._acts) -1
        hesitate = "..."
        if count >= self.max_acts:
            self._acts[count] = "{} {}".format(hesitate, self._acts[count])
        
        verb = "catch" if count < 3 else "carry"

        clown_considered = f"Can {self.clown} {verb} {self._acts[1]}"
        carried_acts = [f" and {act}" for act in self._acts[2:]]

        clown_considered += "".join(carried_acts)
        print(f"{clown_considered}?")

    def _catch_character(self, character: str) -> None:
        """
        Prints out the top act caught the character.

        Args:
            character (str): the caught character
        """
        if len(self._acts) > self.max_acts:
            return
        
        catcher, caught = self._acts[-2], character
        verb = "catch" if catcher[-1] == 's' else "catches"
        print("{} {} {}.".format(catcher.capitalize(), verb, caught))

    def _continue_show(self) -> None:
        """
        This loops through the remaining characters.

        Each character is called, added to the _acts, and carried.
        """
        for character in self.circus[len(self._acts):]:
            self._call_character(character)
            self._acts.append(character)
            self._carry_the_character(character)

    def _carry_the_character(self, character: str) -> None:
        """
        The character is caught and carried.

        Args:
            character (str): The current character to be caught and carried.
        """
        count = len(self._acts)
        self._catch_character(character)

        if count == 3:
            self._carry_current()
        elif count % 2 == 0:
            self._consider_to_carry()
            self._try_to_carry()

    def _carry_current(self):
        """Prints out the current acts Clarence is carrying."""
        clown_carrier ="{} carrying {}".format(self.clown, self._acts[1])
        current_acts = [f" and {act}. " for act in self._acts[2:]]
        clown_carrier += "".join(current_acts)
        print(f"{clown_carrier}")

    def _try_to_carry(self) -> None:
        """
        Clarence Clown tries to carry the current characters

        If Clarence Clown can carry the current characters, a confirmation is printed.
        Else the program cancels.

        Raises:
            Exception: If the number of carried acts is greater than the maximum acts.
        """
        try:
            if len(self._acts) > self.max_acts:
                raise Exception("Cancel!")
            
            print("Yes. {} can.".format(self.clown))
        except:
            CRASH, RESET = "\033[91m", "\033[0m"
            print("{}CRASH \nNo. {} can't. {}".format(CRASH, self.clown, RESET))


clown = Clown()
clown.send_in_the_clown()