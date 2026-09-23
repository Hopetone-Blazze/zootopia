import json


def load_data(file_path):
    """Loads a JSON file and returns its content."""
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_template(file_path):
    """Reads an HTML template file and returns its content as a string."""
    with open(file_path, "r") as handle:
        return handle.read()


def write_html(file_path, content):
    """Writes the given content to an HTML file."""
    with open(file_path, "w") as handle:
        handle.write(content)


def serialize_animal(animal_obj):
    """Serialize a single animal object into an HTML list item.

    Fields that are missing (diet, location, type) are simply skipped.
    """
    characteristics = animal_obj.get("characteristics", {})
    name = animal_obj.get("name")
    diet = characteristics.get("diet")
    locations = animal_obj.get("locations", [])
    animal_type = characteristics.get("type")

    output = '<li class="cards__item">\n'
    output += f'  <div class="card__title">{name}</div>\n'
    output += '  <p class="card__text">\n'

    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'
    if animal_type:
        output += f'      <strong>Type:</strong> {animal_type}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def generate_animals_string(animals_data):
    """Builds the combined HTML string for all animals in the data."""
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
    return output


def main():
    """Reads the data + template, generates the animals HTML, and writes it out."""
    animals_data = load_data("animals_data.json")
    animals_string = generate_animals_string(animals_data)

    template = read_template("animals_template.html")
    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_string)

    write_html("animals.html", final_html)
    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
