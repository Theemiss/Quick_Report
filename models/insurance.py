from api.v1.app import db
from sqlalchemy.orm import relationship
from models.base import BaseModel


from uuid import uuid4


class Insurance(db.Model, BaseModel):
    id = db.Column(db.String(80), primary_key=True)
    Valid = db.Column(db.DateTime)
    car_id = relationship("Car",  uselist=False, backref="insurance")

    def __init__(self, date):
        super().__init__()
        self.id = str(uuid4())
        self.Valid = date
