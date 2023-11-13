#!/usr/bin/python3
"""
file_storage module
"""
import json


"""
class fileStorage
"""


class FileStorage:
    """
    initializing private class attribute which are:
    `__file_path`: path to json file(ex: file.json)
    `__object`: empty dictionary that stores all objects
    by <classname>.id
    """
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """return the dictionary `__object`"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in `__object` the obj with
        key `<obj classname>.id`
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def all_cls(self):
        """Returns a dictionary of valid classes and their references."""
        from models.user import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place

        dt = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place
            }
        return dt

    def save(self):
        """
        serializes the objects and write them into
        json file
        """
        dt = {}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            for key, val in self.__objects.items():
                dt[key] = val.to_dict()
            json.dump(dt, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
                for data in loaded_data.values():
                    cls_name = data.get("__class__")
                    all_cls = self.all_cls()

                    if cls_name in all_cls:
                        cls_obj = all_cls[cls_name]
                        self.new(cls_obj(**data))
        except FileNotFoundError:
            pass
