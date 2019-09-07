import datetime


class Observation:
    """
    Models a single weather observation.

    :author: Johan Nilsson
    :since: 0.1.0
    """
    def __init__(self,
                 date: datetime.date,
                 location: str,
                 temperature: float,
                 precipitation: float,
                 wind_speed: float,
                 cloud_cover: str,
                 forecast: bool = True):
        """
        Initializes this observation object.

        :param date: when this observation was made
        :param location: where the observation was made
        :param temperature: temperature in whichever unit (e.g. °C and °F)
        :param precipitation: amount of precipitation in whichever unit (e.g.
            mm and in)
        :param wind_speed: wind speed in whichever unit (e.g. m/s and mi/hr)
        :param cloud_cover: description of the cloud cover (e.g. sunny, light
            clouds, overcast and heavy rain)
        :param forecast: whether this observation is a forecast or a "true"
            observation, that is an observation made contemporaneously;
            defaults to True (forecast)

        :since: 0.1.0
        """
        self.date = date
        self.location = location
        self.temperature = temperature
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.cloud_cover = cloud_cover
        self.forecast = forecast
