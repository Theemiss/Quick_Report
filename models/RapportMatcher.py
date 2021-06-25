from api.v1.app import db
from models.base import BaseModel
from uuid import uuid4
"""
    Rapport Matcher Model
"""

class ReportCar(db.Model, BaseModel):
    """
        Report Matcher Class and Database Model 
        Holder of two report of Accident
        id : id of the instance
        CAR_A : Report A id
        CAR_B : Report B id 
    """
    id = db.Column(db.String(80), primary_key=True)
    CAR_A = db.Column(db.String(80))
    CAR_B = db.Column(db.String(80))

    def __init__(self, a="", b=""):
        super().__init__()
        self.id = str(uuid4())
        self.CAR_A = a
        self.CAR_B = b
