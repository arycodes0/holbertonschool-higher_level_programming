import json

"""Module for basic serialization of a dictionary to a JSON file"""


def serialize_and_save_to_file(data, filename):
    """
    Here we serialize the given dict and saves it to the JSON file.

    Parameters:
    data(dictionary): A Python Dictionary with data.

    filename(string): The filename of the output JSON file. If the
    output file already exists it should be replaced.
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Here we load and deserialize data from the JSON file.

    Parameters:
    filename(string): The filename of the input JSON file.

    Return:
    dictionary: A Python dictionary with the deserialized
    JSON data from the file.
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
