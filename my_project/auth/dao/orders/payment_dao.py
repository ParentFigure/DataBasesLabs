from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.payment import Payment


class PaymentDAO(GeneralDAO):
    """
    Implementation of Payment data access layer.
    """
    _domain_type = Payment

    def find_by_reservation(self, reservation_id: int) -> List[Payment]:
        return self._session.query(Payment).filter(Payment.reservation_id == reservation_id).all()

    def find_by_status(self, status: str) -> List[Payment]:
        return self._session.query(Payment).filter(Payment.status == status).all()
