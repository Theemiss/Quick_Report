from api.v1.app import db
from models.base import BaseModel
"""
    Feedback model
"""

from uuid import uuid4


class Feedback(db.Model, BaseModel):
    """
        Feedback Class and Database Table
        id : id of instance
        descreption : Company Replis for The Repport
        reports : Report Feedback Relationship
    """
    id = db.Column(db.String(80), primary_key=True)
    description = db.Column(db.String(180))
    reports = db.Column(
        db.String(120), db.ForeignKey('report.id'), nullable=False)

    def __init__(self, description, rapport):
        """
            __init__
        """
        super().__init__()
        self.id = str(uuid4())
        self.description = description
        self.rapport = rapport
