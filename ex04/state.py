import sys


def find_state():
    """
    Finds and prints the state corresponding to a given capital city.
    If the capital city is not found, prints 'Unknown capital city'.
    """

    # Dictionary mapping state names to their abbreviations
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    # Dictionary mapping state abbreviations to their capital cities
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Check that exactly one argument is provided
    if len(sys.argv) != 2:
        return

    # Retrieve the input argument (the capital city)
    capital_name = sys.argv[1]

    # Find the state code corresponding to the capital city
    state_code = None
    for code, capital in capital_cities.items():
        if capital == capital_name:
            state_code = code
            break

    # Print the corresponding state or an error message
    if state_code:
        # If the state code exists, find and print the state name
        for state, code in states.items():
            if code == state_code:
                print(state)
                return
    else:
        # If no state code was found, print an error message
        print("Unknown capital city")


if __name__ == "__main__":
    find_state()
