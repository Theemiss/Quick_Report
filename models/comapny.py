from uuid import uuid4
from api.v1.app import db
from models.base import BaseModel


class Company(db.Model, BaseModel):
    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    tokens = db.relationship('Users', backref='Company', lazy=True)
    raports = db.relationship('Report', backref='Company', lazy=True)
    
    def __init__(self, name):
        super().__init__()
        self.id = str(uuid4())
        self.name = name
