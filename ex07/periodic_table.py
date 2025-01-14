def parse_periodic_table(file_path):
    """
    Reads and parses the periodic_table.txt file.
    Returns a list of dictionaries containing element data.
    """
    elements = []
    with open(file_path, "r") as file:
        for line in file:
            elem_name, attributes = line.strip().split(" = ")
            elem_data = dict(attr.split(":")
                             for attr in attributes.split(", "))
            elem_data["name"] = elem_name
            elements.append(elem_data)
    return elements


def generate_table_body(elements):
    """
    Generates the HTML table body for the periodic table.
    Correctly places elements and ensures proper handling of empty cells.
    """
    TEMPLATE = """
    <td class="element">
        <h4>{name}</h4>
        <ul>
            <li class="number">No. {number}</li>
            <li class="symbol">{small}</li>
            <li class="mass">{molar}</li>
            <li class="electrons">{electron} electron</li>
        </ul>
    </td>
    """

    body = "<tr>"
    position = 0  # Start from position 0

    for dic in elements:
        # Start a new row if current position exceeds the element's position
        if position > int(dic["position"]):
            body += "</tr>\n<tr>"
            position = 0

        # Add empty cells for missing positions
        for _ in range(position, int(dic["position"]) - 1):
            body += "<td class='empty'></td>\n"

        # Update position to current element's position
        position = int(dic["position"])

        # Add the current element to the table
        body += TEMPLATE.format(
            name=dic["name"],
            number=dic["number"],
            small=dic["small"],
            molar=dic["molar"],
            electron=dic["electron"],
        )

    body += "</tr>\n"  # Close the last row
    return body


def generate_html(elements):
    """
    Generates the complete HTML file for the periodic table.
    """
    body = generate_table_body(elements)

    HTML = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Periodic Table</title>
        <style>
            table {{
                border-collapse: collapse;
                margin: auto;
                width: 90%;
            }}
            td {{
                border: 1px solid black;
                width: 100px;
                height: 120px;
                text-align: center;
                vertical-align: top;
                padding: 5px;
            }}
            .element {{
                background-color: #f0f8ff;
                font-size: 0.9em;
                }}
            .symbol {{
                font-size: 1.5em;
                font-weight: bold;
                color: #B22222;
            }}
            .empty {{
                background-color: #e0e0e0;
            }}
            h4 {{
                margin: 5px 0;
                font-size: 1.2em;
                color: #005580;
                font-weight: bold;
            }}
            ul {{
                list-style: none;
                padding: 0;
                margin: 0;
            }}
        </style>
    </head>
    <body>
        <h1 style="text-align: center;">Periodic Table</h1>
        <table>
            {body}
        </table>
    </body>
    </html>
    """

    # Write the HTML file
    with open("periodic_table.html", "w") as file:
        file.write(HTML)

    print("HTML file 'periodic_table.html' generated successfully.")


def main():
    """
    Main function to handle the workflow of parsing and
    generating the HTML file.
    """
    # Ensure the file is in the same directory
    file_path = "periodic_table.txt"

    # Step 1: Parse the periodic table file
    elements = parse_periodic_table(file_path)

    # Step 2: Generate the HTML file
    generate_html(elements)


if __name__ == "__main__":
    main()
