import xml.etree.ElementTree as ET

"""Module that applies serialization and deserialization using XML
as an alternative format to json."""


def serialize_to_xml(dictionary, filename):
    """
    Here we serialize a dictionary to an XML file.

    Parameters:
    dictionary: Dictionary to serialize.
    filename(string): The name of the file to save the XML to.

    Return:
    None
    """

    def add_dict_items(parent, d):
        """
        Here we add the dictionary items to the XML tree.

        Parameters:
        parent(element): The parent XML element.
        d(dictionary): The dictionary to add to the XML tree.

        Return:
        None
        """
        for key, value in d.items():
            element = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_dict_items(element, value)
            else:
                element.text = str(value)

    root = ET.Element("data")
    add_dict_items(root, dictionary)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Here we deserialize an XML file to a dictionary.

    Parameter:
    filename(string): The name of the XML file to read.

    Return:
    dict: The converted dictionary.
    """

    def parse_element(element):
        """
        Here we convert XML element and its children to a dictionary.

        Parameter:
        element: The XML element to convert.

        Return:
        dict: The converted dictionary.
        """
        parsed_dict = {}
        for child in element:
            if len(child) > 0:
                parsed_dict[child.tag] = parse_element(child)
            else:
                parsed_dict[child.tag] = child.text
        return parsed_dict

    tree = ET.parse(filename)
    root = tree.getroot()
    return parse_element(root)


if __name__ == "__main__":
    data = {
        "name": "Ary",
        "age": 29,
        "address": {"street": "401 Ash St", "city": "Lake Oswego"},
    }

    """Serialize to XML."""
    serialize_to_xml(data, "data.xml")

    """Deserialize from XML"""
    deserialized_data = deserialize_from_xml("data.xml")
    print(deserialized_data)
