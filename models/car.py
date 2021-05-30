
from uuid import uuid4
from api.v1.app import db
from models.base import BaseModel


class Car(db.Model, BaseModel):
    id = db.Column(db.String(80), primary_key=True)  # matricule number
    type_c = db.Column(db.String(30), nullable=False)
    Mark = db.Column(db.String(30))
    CIN = db.Column(db.String(30))
    insurred = db.Column(db.Boolean, default=False)
    insurance_id = db.Column(db.String(120), db.ForeignKey(
        'insurance.id'), nullable=False)
    raports = db.relationship('Report', backref='Car', lazy=True)

    def __init__(self, type_c="", mark="", cin="", ins=""):
        super().__init__()
        self.id = str(uuid4())
        self.type_c = type_c
        self.Mark = mark
        self.CIN = cin
        self.insurance_id = ins
