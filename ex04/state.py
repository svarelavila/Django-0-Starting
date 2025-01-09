import sys

def find_state():
    # Diccionarios
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

    # Verificar que se pase exactamente un argumento
    if len(sys.argv) != 2:
        return

    # Obtener el argumento
    capital_name = sys.argv[1]

    # Buscar el estado correspondiente a la capital
    state_code = None
    for code, capital in capital_cities.items():
        if capital == capital_name:
            state_code = code
            break

    # Mostrar el resultado
    if state_code:
        for state, code in states.items():
            if code == state_code:
                print(state)
                return
    else:
        print("Unknown capital city")

if __name__ == "__main__":
    find_state()


"""
import sys

def find_state():
    """
    Finds and prints the state corresponding to a given capital city.
    If the capital city does not exist, prints 'Unknown capital city'.
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

    # Ensure exactly one argument is provided
    if len(sys.argv) != 2:
        return

    capital_name = sys.argv[1]

    # Find the state code using a generator
    state_code = next((code for code, capital in capital_cities.items() if capital == capital_name), None)

    # Print the state name or an error message
    print(next((state for state, code in states.items() if code == state_code), "Unknown capital city"))

if __name__ == "__main__":
    find_state()
"""