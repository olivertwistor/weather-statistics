from ui.input_form import InputForm


class AddObservation(InputForm):
    """
    Input form used for adding an observation.

    :author: Johan Nilsson
    :since:  0.1.0
    """

    def __init__(self):
        super().__init__()

    def show_form(self):
        print("Add observation")
        print("---------------")
        print()

        # Date.
        self.user_input["date"] = self.date_input(
            "Date of this observation (YYYY-MM-DD): ")

        # Location.
        self.user_input["location"] = self.string_input(
            "Location of this observation: ")

        # Temperature.
        self.user_input["temperature"] = self.float_input(
            "Temperature in whichever unit (decimal values are okay): ")

        # Precipitation.
        self.user_input["precipitation"] = self.float_input(
            "Precipitation in whichever unit (decimal values are okay): ")

        # Wind speed.
        self.user_input["wind_speed"] = self.float_input(
            "Wind speed in whichever unit (decimal values are okay): ")

        # Cloud cover.
        self.user_input["cloud_cover"] = self.string_input(
            "Cloud cover (e.g. 'sunny', 'overcast', 'heavy rain', "
            "'partially cloudy'): ")

        # Forecast.
        self.user_input["forecast"] = self.boolean_input(
            "Is this a forecast instead of an actual observation (Y for "
            "forecast, N for observation)? ")
