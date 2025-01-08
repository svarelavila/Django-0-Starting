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

