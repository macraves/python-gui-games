"""Tic Tac Toe Player Class"""


class Player:
    """Represents a player in the Tic Tac Toe game."""

    valid_signs = ["X", "O"]

    @classmethod
    def is_valid_sign(cls, sign: str) -> bool:
        """Check if the given sign is valid.
        Args:
            sign (str): The sign to check.
        Returns:
            bool: True if the sign is valid, False otherwise.
        """
        if sign not in cls.valid_signs:
            return False
        return True

    def __init__(self, name: str, sign: str):
        """Initialize a Player instance.
        Args:
            name (str): The name of the player.
            sign (str): The sign of the player ('X' or 'O').
        Raises:
            KeyError: If the sign is not valid.
        """
        self.name = name
        self.sign = sign

    @property
    def sign(self):
        """Get the sign of the player.
        Returns:
            str: The sign of the player.
        """
        return self._sign

    @sign.setter
    def sign(self, value):
        """Set the sign of the player.
        Args:
            value (str): The sign to set.
        Raises:
            KeyError: If the sign is not valid.
        """
        value = value.upper()
        if not self.is_valid_sign(value):
            raise KeyError("Valid signs are 'X' or 'O'. Please choose one of them.")
        self._sign = value
        

