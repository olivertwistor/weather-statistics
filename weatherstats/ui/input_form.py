import datetime
from abc import ABC, abstractmethod


class InputForm(ABC):
    """
    Base class for input forms.

    :author: Johan Nilsson
    :since:  0.1.0
    """
    def __init__(self):
        """
        Initializes a dictionary for holding the user inputs.

        :since: 0.1.0
        """
        self.user_input = {}

    @abstractmethod
    def show_form(self):
        """
        Shows the input form to the user. As the user enters input, it's stored
        in the self.user_input dictionary.

        :since: 0.1.0
        """
        pass

    @staticmethod
    def boolean_input(prompt: str) -> bool:
        """
        Asks the user for input and returns a bool matching the input.

        Acceptable input for True is "true", "yes", "y" or 1 (case
        insensitive). Every other input is interpreted as False.

        :param prompt: the input prompt to show the user

        :return: A bool matching user input.
        :rtype:  bool

        :since: 0.1.0
        """
        user_input = input(prompt).strip().lower()

        if user_input in ["true", "yes", "y", 1]:
            return True

        return False

    @staticmethod
    def date_input(prompt: str) -> datetime.date:
        """
        Asks the user for input in the form YYYY-MM-DD and returns a
        datetime.date object matching the input.

        :param prompt: the input prompt to show the user

        :return: A datetime.date object matching user input; or today's date if
                 user input is malformed.
        :rtype:  datetime.date

        :since: 0.1.0
        """
        user_input = input(prompt).strip()
        year, month, day = map(int, user_input.split("-"))

        try:
            return datetime.date(year, month, day)
        except ValueError:
            return datetime.date.today()

    @staticmethod
    def float_input(prompt: str) -> float:
        """
        Asks the user for input and returns a float matching the input.

        :param prompt: the input prompt to show the user

        :return: A float matching user input; or 0.0 if user input is malformed.
        :rtype:  float

        :since: 0.1.0
        """
        user_input = input(prompt).strip()

        try:
            return float(user_input)
        except ValueError:
            return 0.0

    @staticmethod
    def string_input(prompt: str) -> str:
        """
        Asks the user for input and returns that input.

        :param prompt: the input prompt to show the user

        :return: User input, stripped from surrounding whitespace.
        :rtype:  str

        :since: 0.1.0
        """
        user_input = input(prompt).strip()

        return user_input
