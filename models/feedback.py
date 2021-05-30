from api.v1.app import db
from models.base import BaseModel


from uuid import uuid4

class Feedback(db.Model,BaseModel):
    id = db.Column(db.String(80), primary_key=True)
    desscreption = db.Column(db.String(180))
    rapport = db.Column(
        db.String(120), db.ForeignKey('report.id'), nullable=False)

    def __init__(self, desscreption, rapport):
        super().__init__()
        self.id = str(uuid4())
        self.desscreption = desscreption
        self.rapport = rapport
