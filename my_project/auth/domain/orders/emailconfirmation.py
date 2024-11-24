from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class EmailConfirmation(db.Model, IDto):
    __tablename__ = "emailconfirmation"

    confirmation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    email_sent_date = db.Column(db.DateTime, nullable=False)
    confirmation_status = db.Column(db.Enum("pending", "confirmed", "failed"), nullable=False)

    user = db.relationship("User", backref="email_confirmations")

    def __repr__(self) -> str:
        return f"EmailConfirmation({self.confirmation_id}, {self.user_id}, '{self.confirmation_status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "confirmation_id": self.confirmation_id,
            "user_id": self.user_id,
            "email_sent_date": self.email_sent_date.isoformat(),
            "confirmation_status": self.confirmation_status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmailConfirmation:
        return EmailConfirmation(**dto_dict)
