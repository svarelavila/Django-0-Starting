def display_numbers():
    # Abrir y leer el archivo numbers.txt
    try:
        with open("numbers.txt", "r") as file:
            # Leer el contenido y separar los números por coma
            content = file.read()
            numbers = content.split(",")  # Convertir en una lista
            
            # Imprimir cada número en una nueva línea
            for number in numbers:
                print(number.strip())  # Quitar espacios en blanco si los hay
    except FileNotFoundError:
        print("Error: El archivo numbers.txt no existe.")

if __name__ == "__main__":
    display_numbers()
