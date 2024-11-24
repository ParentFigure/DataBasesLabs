from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Reservation(db.Model, IDto):
    __tablename__ = "reservation"

    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.hotel_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum("pending", "confirmed", "cancelled"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.room_id"), nullable=False)

    user = db.relationship("User", backref="reservations")
    room = db.relationship("Room", backref="reservations")

    def __repr__(self) -> str:
        return f"Reservation({self.reservation_id}, {self.user_id}, {self.room_id}, '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "reservation_id": self.reservation_id,
            "hotel_id": self.hotel_id,
            "user_id": self.user_id,
            "start_date": self.start_date.isoformat(),
            "end_date": self.end_date.isoformat(),
            "status": self.status,
            "room_id": self.room_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservation:
        return Reservation(**dto_dict)