from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Room(db.Model, IDto):
    __tablename__ = "room"

    room_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey("hotel.hotel_id"), nullable=False)
    room_type = db.Column(db.Enum("single", "double", "suite"), nullable=False)
    price_per_night = db.Column(db.DECIMAL(10, 2), nullable=False)
    availability = db.Column(db.Boolean, nullable=False)

    hotel = db.relationship("Hotel", backref="rooms")

    def __repr__(self) -> str:
        return f"Room({self.room_id}, '{self.room_type}', {self.price_per_night}, '{self.availability}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "room_id": self.room_id,
            "hotel_id": self.hotel_id,
            "room_type": self.room_type,
            "price_per_night": float(self.price_per_night),
            "availability": self.availability,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Room:
        return Room(**dto_dict)