def sort_musicians():
    """
    Sorts and prints the names of musicians by year (ascending),
    then alphabetically for similar years.
    """
    # Dictionary with musicians and their birth years
    d = {
        'Hendrix': '1942',
        'Allman': '1946',
        'King': '1925',
        'Clapton': '1945',
        'Johnson': '1911',
        'Berry': '1926',
        'Vaughan': '1954',
        'Cooder': '1947',
        'Page': '1944',
        'Richards': '1943',
        'Hammett': '1962',
        'Cobain': '1967',
        'Garcia': '1942',
        'Beck': '1944',
        'Santana': '1947',
        'Ramone': '1948',
        'White': '1975',
        'Frusciante': '1970',
        'Thompson': '1949',
        'Burton': '1939',
    }

    # Sorting the dictionary:
    # Transform dictionary items into a list of tuples and sort them
    # The key function sorts first by year (x[1]) and then alphabetically by name (x[0])
    sorted_musicians = sorted(d.items(), key=lambda x: (x[1], x[0]))

    # Print only the musician names in the desired order
    for musician, _ in sorted_musicians:
        print(musician)

if __name__ == "__main__":
    sort_musicians()
