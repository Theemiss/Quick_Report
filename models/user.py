from api.v1.app import db
from models.base import BaseModel
from passlib.apps import custom_app_context as pwd_context
from uuid import uuid4
"""
User Model
"""

class Users(db.Model, BaseModel):
    """
        User(s: Postress Problem) Class and Database Table
        id: id of the user
        email : Email Address user for login
        password_hash : Password used to login (Hashed)
        first_name : First Name
        last_name : Last Name
        phone : Phone Number
        adresse : Home address of the user
        permit_id : Permit id
        permit_validation : Data of the Permit
        Company_token : id of the Company that the user belong Too 
                        Company user Relationship
        repports : Report user Relationship
    """
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
    reports = db.relationship('Report', backref='Users', lazy=True)

    def __init__(self, email, token, f_name="", l_name="", phone="", car_id="", p_id="", p_v="", cin="", addr=""):
        """
            __init__
        """
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
        """
        hash password using Hashlib
        """
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """
            Check password with the hasshed one
        """
        return pwd_context.verify(password, self.password_hash)
