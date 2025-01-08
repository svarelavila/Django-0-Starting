import sys

def find_capital():
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
    state_name = sys.argv[1]

    # Buscar la capital correspondiente
    state_code = states.get(state_name)
    if state_code:
        print(capital_cities[state_code])
    else:
        print("Unknown state")

if __name__ == "__main__":
    find_capital()
