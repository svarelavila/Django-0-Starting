import sys


def print_state(city: str):
    # Diccionarios proporcionados
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
    
    # Buscar el código del estado a partir de la capital
    state_code = None
    for code, capital in capital_cities.items():
        if capital == city:
            state_code = code
            break
    
    # Si no se encontró la capital, mostrar el mensaje correspondiente
    if not state_code:
        print("Unknown capital city")
        return
    
    # Buscar el nombre del estado a partir del código
    for state, code in states.items():
        if code == state_code:
            print(state)
            return

def main():
    # Verificar que haya exactamente un argumento
    if len(sys.argv) == 2:
        print_state(sys.argv[1])  # Llamamos a la función con el argumento de la ciudad

if __name__ == '__main__':
    main()
