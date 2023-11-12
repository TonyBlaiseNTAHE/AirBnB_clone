#!/usr/bin/python3

"""
user module
"""

from models.base_model import BaseModel

"""
User class
"""


class User(BaseModel):
    """
    user attributes
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        """ class constructor"""
        super().__init__(*args, **kwargs)