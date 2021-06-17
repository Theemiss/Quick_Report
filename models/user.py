from api.v1.app import db
from models.base import BaseModel
from passlib.apps import custom_app_context as pwd_context
from uuid import uuid4


class Users(db.Model, BaseModel):
    id = db.Column(db.String(120), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    CIN = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200))
    authenticated = db.Column(db.Boolean, default=False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    phone = db.Column(db.String(30))
    adresse = db.Column(db.String(30))
    permit_id = db.Column(db.String(30), unique=True)
    permit_validation = db.Column(db.DateTime)
    comany_token = db.Column(
        db.String(120), db.ForeignKey('company.id'), nullable=False)
    raports = db.relationship('Report', backref='Users', lazy=True)

    def __init__(self, email, token, f_name="", l_name="", phone="", car_id="", p_id="", p_v="", cin="", addr=""):
        super().__init__()
        self.id = str(uuid4())
        self.CIN = cin
        self.email = email
        self.comany_token = token
        self.first_name = f_name
        self.last_name = l_name
        self.phone = phone
        self.car_id = car_id
        self.permit_id = p_id
        self.permit_validation = p_v
        self.adresse = addr

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
