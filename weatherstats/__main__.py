import sys

from models.observation import Observation
from ui.add_observation import AddObservation


def main():
    """
    Main program flow.

    :since: 0.1.0
    """
    add_observation = AddObservation()
    add_observation.show_form()
    observation = Observation.from_dictionary(add_observation.user_input)
    sys.exit(0)


if __name__ == '__main__':
    main()
