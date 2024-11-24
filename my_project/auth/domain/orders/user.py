from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    account_status = db.Column(db.Enum("active", "inactive", "suspended"), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"User({self.user_id}, '{self.username}', '{self.email}', '{self.account_status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "account_status": self.account_status,
            "registration_date": self.registration_date.isoformat(),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        return User(**dto_dict)