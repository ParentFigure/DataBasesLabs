from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Payment(db.Model, IDto):
    __tablename__ = "payment"

    payment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey("reservation.reservation_id"), nullable=False)
    amount = db.Column(db.DECIMAL(10, 2), nullable=False)
    status = db.Column(db.Enum("pending", "completed", "failed"), nullable=False)

    reservation = db.relationship("Reservation", backref="payments")

    def __repr__(self) -> str:
        return f"Payment({self.payment_id}, {self.reservation_id}, {self.amount}, '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "payment_id": self.payment_id,
            "reservation_id": self.reservation_id,
            "amount": float(self.amount),
            "status": self.status,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Payment:
        return Payment(**dto_dict)
