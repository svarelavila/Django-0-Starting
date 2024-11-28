def sort_musicians_by_year():
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
    
    # Ordenamos el diccionario primero por el año y luego alfabéticamente por el nombre
    sorted_musicians = sorted(d.items(), key=lambda x: (x[1], x[0]))
    
    # Imprimimos solo los nombres, uno por línea
    for musician in sorted_musicians:
        print(musician[0])

if __name__ == '__main__':
    sort_musicians_by_year()
