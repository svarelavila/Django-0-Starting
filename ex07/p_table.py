def parse_line(line: str):
    """Procesa una línea del archivo de entrada y devuelve un diccionario con los datos."""
    el = line.split("=")
    result = dict((value.strip().split(":") for value in el[1].split(", ")))
    result["name"] = el[0].strip()
    return result

def generate_table_body(elements):
    """Genera el cuerpo de la tabla HTML con los elementos proporcionados."""
    TEMPLATE = """
    <td class="element">
        <h4>{name}</h4>
        <ul>
            <li class="number">No {number}</li>
            <li class="symbol">{small}</li>
            <li class="mass">{molar}</li>
            <li class="electrons">{electron} electron</li>
        </ul>
    </td>
    """
    
    body = "<tr>"
    position = 0  # Inicializamos la posición en 0
    
    for dic in elements:
        # Si la posición actual es mayor que la de este elemento, hacemos salto de línea
        if position > int(dic["position"]):
            body += "    </tr>\n    <tr>"
            position = 0
        
        # Añadir celdas vacías si es necesario
        for _ in range(position, int(dic["position"]) - 1):
            body += "      <td class='empty'></td>\n"
        
        position = int(dic["position"])

        # Añadir el elemento a la tabla
        body += TEMPLATE.format(
            name=dic["name"],
            number=dic["number"],
            small=dic["small"],
            molar=dic["molar"],
            electron=dic["electron"],
        )
    
    body += "    </tr>\n"
    return body

def generate_html(body):
    """Genera el archivo HTML completo insertando el cuerpo de la tabla en la estructura HTML base."""
    HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Periodic Table</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          margin: 20px;
          background-color: #f4f4f4;
        }}
        table {{
          border-collapse: collapse;
          margin: auto;
          width: 80%;
        }}
        td {{
          text-align: center;
          padding: 10px;
          border: 1px solid black;
          width: 80px;
          height: 100px;
          background-color: #d3d3d3;
        }}
        .element {{
          background-color: #add8e6;
          padding: 5px;
          font-size: 0.9em;
        }}
        .element h4 {{
          margin: 5px 0;
          font-size: 1.2em;
          color: black;
        }}
        .element ul {{
          padding: 0;
          margin: 0;
          list-style: none;
        }}
      </style>
    </head>
    <body>
      <h1 style="text-align: center;">Tabla Periódica</h1>
      <table>
        {body}
      </table>
    </body>
    </html>
    """
    # Escribir el archivo HTML con el cuerpo generado
    with open("periodic_table.html", "w") as f:
        f.write(HTML.format(body=body))

def main():
    """Función principal para leer el archivo, procesar los datos y generar el HTML."""
    # Leer el archivo y procesar las líneas
    with open("periodic_table.txt", "r") as f:
        elements = [parse_line(line.strip()) for line in f.readlines()]
    
    # Generar el cuerpo de la tabla con los elementos procesados
    table_body = generate_table_body(elements)
    
    # Generar y escribir el archivo HTML final
    generate_html(table_body)

if __name__ == "__main__":
    main()
