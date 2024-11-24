from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.reservation import Reservation


class ReservationDAO(GeneralDAO):
    """
    Implementation of Reservation data access layer.
    """
    _domain_type = Reservation

    def find_by_user(self, user_id: int) -> List[Reservation]:
        return self._session.query(Reservation).filter(Reservation.user_id == user_id).all()

    def find_by_status(self, status: str) -> List[Reservation]:
        return self._session.query(Reservation).filter(Reservation.status == status).all()
