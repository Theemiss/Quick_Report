#!/usr/bin/python3
"""
Contains the class DBStorage
"""
from models.comapny import Company
from models.user import Users
from models.car import Car
from models.insurance import Insurance
from models.report import Report

classes = {"Company": Company, "Users": Users,
           "Car": Car, "Insurance": Insurance, "Report": Report}


def all(cla):
    """query on the current database session"""
    new_dict = {}
    objs = cla.query.all()
    for obj in objs:
        k = obj.to_dict()
        key = obj.__class__.__name__ + '.' + obj.id
        new_dict[key] = k
    return (new_dict)


def get_id(cls, id):
    """
    Returns the object based on the class name and its ID, or
    None if not found
    """
    if cls not in classes.values():
        return None
    new_dict = all(cls)
    for value in new_dict.values():
        print(value)
        if (value['id'] == id):
            return value

    return None
