import pickle

"""Learning to serialize and deserialize, creating a
custom class with the given attributes."""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        """
        Here we serialize the current instance and save it to
        the provided filename.

        Parameter:
        filename(string): The filename where the object
        will be serialized.
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as error:
            print(f"Error during serialization: {error}")

    @classmethod
    def deserialize(cls, filename):
        """
        Here we deserialize an instance from the provided filename.

        Parameter:
        filename(string): The filename from where the object will
        be deserialized.

        Return:
        CustomObject: An instance of the CustomObject from the provided filename.
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except Exception as error:
            print(f"Error during deserialization: {error}")
            return None
