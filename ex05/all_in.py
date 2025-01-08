import sys

def process_input():
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

    # Crear un diccionario inverso de capitales a estados
    capitals_to_states = {capital: state for state, code in states.items() for code, capital in capital_cities.items() if code == states[state]}

    # Obtener la entrada del usuario
    if len(sys.argv) != 2:
        return

    input_string = sys.argv[1]
    expressions = [expr.strip() for expr in input_string.split(',')]

    for expr in expressions:
        if not expr:  # Ignorar expresiones vacías
            continue
        
        # Buscar como estado
        if expr in states:
            state_code = states[expr]
            capital = capital_cities[state_code]
            print(f"{capital} is the capital of {expr}")
        # Buscar como capital
        elif expr in capitals_to_states:
            state = capitals_to_states[expr]
            print(f"{expr} is the capital of {state}")
        # Entrada desconocida
        else:
            print(f"{expr} is neither a capital city nor a state")

if __name__ == "__main__":
    process_input()



"""
import sys

def process_input(input_str: str):
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

    def normalize_string(s):
        return " ".join(s.split()).strip().lower()

    expressions = input_str.split(',')
    
    # Si hay comas consecutivas (,,), no hacer nada
    if ',,' in input_str:
        return

    results = []

    for expr in expressions:
        expr_normalized = normalize_string(expr)

        if expr_normalized == '':
            continue
        
        found = False
        
        # Comprobar si la expresión es un estado
        for state, code in states.items():
            if normalize_string(state) == expr_normalized:
                results.append(f"{capital_cities[code]} is the capital of {state}")
                found = True
                break
        
        # Comprobar si la expresión es una capital
        if not found:
            for abbr, city in capital_cities.items():
                if normalize_string(city) == expr_normalized:
                    state = [state for state, code in states.items() if code == abbr][0]
                    results.append(f"{city} is the capital of {state}")
                    found = True
                    break
        
        # Si no es ni estado ni capital
        if not found:
            results.append(f"{expr.strip()} is neither a capital city nor a state")
    
    # Imprimir todos los resultados
    for result in results:
        print(result)

def main():
    # Validar que haya exactamente un argumento
    if len(sys.argv) == 2:
        input_str = sys.argv[1]
        
        # Verificar que no haya comas consecutivas
        if ',,' in input_str:
            return
        
        process_input(input_str)

if __name__ == '__main__':
    main()
"""