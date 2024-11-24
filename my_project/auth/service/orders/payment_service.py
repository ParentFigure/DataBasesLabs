from typing import List
from my_project.auth.dao.orders.payment_dao import PaymentDAO
from my_project.auth.service.general_service import GeneralService


class PaymentService(GeneralService):
    """
    Implementation of Payment service.
    """
    _dao = PaymentDAO()

    def find_by_reservation(self, reservation_id: int) -> List[object]:
        """
        Gets Payment objects from the database by reservation ID.
        :param reservation_id: reservation ID value
        :return: list of Payment objects
        """
        return self._dao.find_by_reservation(reservation_id)

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets Payment objects from the database by status.
        :param status: status value
        :return: list of Payment objects
        """
        return self._dao.find_by_status(status)
