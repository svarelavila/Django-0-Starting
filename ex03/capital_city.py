import sys


def capital_city(state_name: str):
    # Diccionarios de estados y sus capitales
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
    
    # Obtener la abreviatura del estado
    state_abbreviation = states.get(state_name)
    
    if not state_abbreviation:
        print("Unknown state")
        return
    
    # Imprimir la capital correspondiente
    print(capital_cities.get(state_abbreviation))


def main():
    # Verifica si hay exactamente un argumento
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])  # Llamada a la función con el estado como argumento

if __name__ == '__main__':
    main()
