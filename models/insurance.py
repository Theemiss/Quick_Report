from api.v1.app import db
from sqlalchemy.orm import relationship
from models.base import BaseModel
"""
    insurance of the Car Model
"""

from uuid import uuid4


class Insurance(db.Model, BaseModel):
    """
        insurance Class and Database model
        valid : Time Valideties for the  insurance
        car_id : Car and insurance Relationship
    """
    id = db.Column(db.String(80), primary_key=True)
    Valid = db.Column(db.DateTime)
    car_id = relationship("Car",  uselist=False, backref="insurance")

    def __init__(self, date):
        """
            __init__
        """
        super().__init__()
        self.id = str(uuid4())
        self.Valid = date
