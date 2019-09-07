from abc import ABC, abstractmethod


class InputForm(ABC):
    """
    Base class for input forms.

    :author: Johan Nilsson
    :since: 0.1.0
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
