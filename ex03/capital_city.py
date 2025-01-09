import sys

def find_capital():
    """
    Finds and prints the capital city of a given state.
    If the state does not exist, prints 'Unknown state'.
    """
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    state_name = sys.argv[1]
    state_code = states.get(state_name)

    if state_code:
        print(capital_cities[state_code])
    else:
        print("Unknown state")

if __name__ == "__main__":
    find_capital()
