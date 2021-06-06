from datetime import datetime
from sqlalchemy import Column, DateTime
from api.v1.app import db


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self):
        """Initialization of the base model"""
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if "password_hash" in new_dict:
            del new_dict["password_hash"]
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        db.session.delete(self)

    def save_to_db(self):

        db.session.add(self)

        db.session.commit()

