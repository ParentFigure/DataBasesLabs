from typing import List
from my_project.auth.dao.orders.reservation_dao import ReservationDAO
from my_project.auth.service.general_service import GeneralService


class ReservationService(GeneralService):
    """
    Implementation of Reservation service.
    """
    _dao = ReservationDAO()

    def find_by_user(self, user_id: int) -> List[object]:
        """
        Gets Reservation objects from the database by user ID.
        :param user_id: user ID value
        :return: list of Reservation objects
        """
        return self._dao.find_by_user(user_id)

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Reservation objects from the database by status.
        :param status: status value
        :return: list of Reservation objects
        """
        return self._dao.find_by_status(status)
