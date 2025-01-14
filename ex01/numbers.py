def print_numbers():
    """
    Reads the file 'numbers.txt', splits its content by commas,
    and prints each number on a new line.
    """
    try:
        # Open the file and read its content
        with open("numbers.txt", "r") as file:
            content = file.read()  # Read the entire file

            # Split the content into numbers using commas
            numbers = content.split(",")

            # Print each number on a new line
            for number in numbers:
                print(number.strip())  # Remove any extra spaces
    except FileNotFoundError:
        # Print an error message if the file doesn't exist
        print("Error: The file 'numbers.txt' does not exist.")


if __name__ == "__main__":
    print_numbers()
