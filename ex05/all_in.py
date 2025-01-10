import sys

def process_input():
    """
    Processes user input to determine if it is a state or a capital city.
    Outputs the relationship between states and capitals, or an error
    message if not found.
    """

    # Dictionary mapping states to their abbreviations
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    # Dictionary mapping abbreviations to their capital cities
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Create an inverted dictionary mapping capitals to states
    capitals_to_states = {
        capital: state for state, code in states.items()
        for code, capital in capital_cities.items()
        if code == states[state]
    }

    # Ensure exactly one argument is provided
    if len(sys.argv) != 2:
        return

    # Retrieve user input and split it by commas
    input_string = sys.argv[1]
    expressions = [expr.strip() for expr in input_string.split(',')]

    # Process each expression
    for expr in expressions:
        if not expr:  # Skip empty expressions
            continue

        # Check if the input matches a state
        if expr in states:
            state_code = states[expr]
            capital = capital_cities[state_code]
            print(f"{capital} is the capital of {expr}")
        # Check if the input matches a capital
        elif expr in capitals_to_states:
            state = capitals_to_states[expr]
            print(f"{expr} is the capital of {state}")
        # Handle unknown input
        else:
            print(f"{expr} is neither a capital city nor a state")

if __name__ == "__main__":
    process_input()
