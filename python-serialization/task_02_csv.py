import csv
import json

"""Module that reads data from one csv format and converts it
into a json format using serialization techniques."""


def convert_csv_to_json(csv_filename):
    """
    Here we convert csv data to Json format and write
    it to data.json.

    Parameter:
    csv_filename(string): The filename of the input csv file.

    Return:
    boolean: True if the conversion was successful, otherwise
    False.
    """
    try:
        # Open the csv file and read the data
        with open(csv_filename, more="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convert rows into a list of dictionaries
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to json format
        with open("data.json", mode="w") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFound:
        print(f"File {csv_filename} not found.")
        return False

    except Exception as error:
        print(f"An error has occurred: {error}")
        return False
