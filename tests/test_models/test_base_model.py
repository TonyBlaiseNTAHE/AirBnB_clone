#!/usr/bin/python3
import unittest
from uuid import uuid4
from datetime import datetime

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
        self.updated_at = datetime.now()
        
    def to_dict(self):
        dt = {}
        dt['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                dt[key] = value.isoformat()
            else:
                dt[key] = value
        return dt

class BaseModelTest(unittest.TestCase):
    
    def test_id(self):
        model = BaseModel()
        self.assertEqual(model.id, model.id)
        mod = BaseModel()
        self.assertEqual(mod.id, mod.id)
        mo = BaseModel()
        self.assertEqual(mo.id, mo.id)
        m = BaseModel()
        self.assertEqual(m, m)
        b = BaseModel()
        self.assertEqual(b.id, b.id)
        a = BaseModel()
        self.assertEqual(a.id, a.id)
    
    def test_updated_at(self):
        model = BaseModel()
        self.assertEqual(model.updated_at, model.updated_at)
        mod = BaseModel()
        self.assertEqual(mod.updated_at, mod.updated_at)
        mod = BaseModel()
        self.assertEqual(mod.updated_at, mod.updated_at)
        mo = BaseModel()
        self.assertEqual(mo.updated_at, mo.updated_at)
        m = BaseModel()
        self.assertEqual(m.updated_at, m.updated_at)
        d = BaseModel()
        self.assertEqual(d.updated_at, d.updated_at)
    
    def test_created_at(self):
        model = BaseModel()
        self.assertEqual(model.created_at, model.created_at)
        mod = BaseModel()
        self.assertEqual(mod.created_at, mod.created_at)
        mod = BaseModel()
        self.assertEqual(mod.created_at, mod.created_at)
        mo = BaseModel()
        self.assertEqual(mo.created_at, mo.created_at)
        m = BaseModel()
        self.assertEqual(m.created_at, m.created_at)
        d = BaseModel()
        self.assertEqual(d.created_at, d.created_at)
        
    def test_save(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    
    

if __name__ == "__main__":
    unittest.main()
    