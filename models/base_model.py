#!/usr/bin/python3

"""
base_model module
"""

import uuid
from datetime import datetime
from models import storage

"""
class BaseModel
"""


class BaseModel:
    """initializing public class attribute
    """
    def __init__(self, *args, **kwargs):
        """initialize class attribute"""
        lst = ['Created_at', 'updated_at']
        if kwargs or kwargs != {}:
            for key, val in kwargs.items():
                if key != '__class__':
                    if key in lst:
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ returns the class name, id and
            dictionary of the instance
        """
        return f"[{self.__class__.__name__}]({self.id}) {self.__dict__}"

    def save(self):
        """ updates the public instance attribute
            `updated_at` with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containning all keys/values
            of __dict__ of the instance
        """
        d = {}
        # loop through the dictionary and insert class key with the
        # class name of the object
        d['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                d[key] = value.isoformat()
            else:
                d[key] = value
            dt = dict(d)
        return dt
