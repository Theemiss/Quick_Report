
from uuid import uuid4
from api.v1.app import db
from models.base import BaseModel


class Report(db.Model, BaseModel):
    id = db.Column(db.String(80), primary_key=True)
    driver_name = db.Column(db.String(30), nullable=False)
    driver_lastname = db.Column(db.String(30), nullable=False)
    driver_adresse = db.Column(db.String(30), nullable=False)
    driver_permit = db.Column(db.String(30), nullable=False)
    driver_permit_valid = db.Column(db.DateTime)
    car_id = db.Column(db.String(120), db.ForeignKey('car.id'), nullable=False)
    client_id = db.Column(
        db.String(120), db.ForeignKey('users.id'), nullable=False)
    compnay_id = db.Column(db.String(120), db.ForeignKey(
        'company.id'), nullable=False)
    feedbacks = db.relationship('Feedback', backref='Report', lazy=True)

    def __init__(self, driver, car, client, company_id, l_name, addr, per, per_v):
        super().__init__()
        self.id = str(uuid4())
        self.driver_name = driver
        self.car_id = car
        self.client_id = client
        self.compnay_id = company_id
        self.driver_lastname = l_name
        self.driver_adresse = addr
        self.driver_permit = per
        self.driver_permit_valid = per_v
