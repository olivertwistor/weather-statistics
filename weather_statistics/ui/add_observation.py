import datetime

from ui.input_form import InputForm


class AddObservation(InputForm):
    """
    Input form used for adding an observation.

    :author: Johan Nilsson
    :since: 0.1.0
    """

    def __init__(self):
        super().__init__()

    def show_form(self):
        print("Add observation")
        print("---------------")
        print()

        # Date.
        try:
            date_input = input("Date of this observation (YYYY-MM-DD): ")
            date_year, date_month, date_day = map(int, date_input.split("-"))
            self.user_input['date'] = datetime.date(
                date_year, date_month, date_day)
        except ValueError:
            print("Wrong input format. Only integers and dashes are allowed.")
            return

        # Location.
        location_input = input("Location of this observation: ")
