import sys

from ui.add_observation import AddObservation


def main():
    """
    Main program flow.

    :since: 0.1.0
    """
    add_observation = AddObservation()
    add_observation.show_form()
    sys.exit(0)


if __name__ == '__main__':
    main()
