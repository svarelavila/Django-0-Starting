def my_var():
    """"
    Initializes variables with different data types
    and prints their values and types.
    """
    # Different types of variables

    variables = [
        42,  # Integer
        "42",  # String
        "quarente-deux",  # Another string
        42.0,  # Float
        True,  # Boolean
        [42],  # List
        {42: 42},  # Dictionary
        (42,),  # Tuple
        set()  # Empty set
    ]
    # Iterete through the list and print value and type
    for var in variables:
        print(f"{var} has a type {type(var)}")


if __name__ == "__main__":
    my_var()
