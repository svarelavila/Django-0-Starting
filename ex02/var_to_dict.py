def var_to_dict():
    # Lista de tuplas (nombre, año)
    d = [
        ('Hendrix', '1942'),
        ('Allman', '1946'),
        ('King', '1925'),
        ('Clapton', '1945'),
        ('Johnson', '1911'),
        ('Berry', '1926'),
        ('Vaughan', '1954'),
        ('Cooder', '1947'),
        ('Page', '1944'),
        ('Richards', '1943'),
        ('Hammett', '1962'),
        ('Cobain', '1967'),
        ('Garcia', '1942'),
        ('Beck', '1944'),
        ('Santana', '1947'),
        ('Ramone', '1948'),
        ('White', '1975'),
        ('Frusciante', '1970'),
        ('Thompson', '1949'),
        ('Burton', '1939')
    ]
    
    # Crear el diccionario acumulando nombres en caso de años duplicados
    my_dict = {}
    for name, year in d:
        if year in my_dict:
            my_dict[year] += f" {name}"  # Concatenar nombres
        else:
            my_dict[year] = name

    # Mostrar el diccionario en el formato requerido
    for year, names in my_dict.items():
        print(f"{year} : {names}")

if __name__ == "__main__":
    var_to_dict()
