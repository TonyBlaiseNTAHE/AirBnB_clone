#!/usr/bin/python3
""" importing uuid module
"""
from  uuid import uuid4
from datetime import datetime
""" class called BaseModel
"""

class BaseModel():
    """initializing the class 
    """
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}]({self.id}){self.__dict__}"
    
    def save(self):
        self.update_at = datetime.now()
        
    def to_dict(self):
        dt = {}
        dt['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dt[key] = value.isoformat()
            else:
                dt[key] = value
        return dt