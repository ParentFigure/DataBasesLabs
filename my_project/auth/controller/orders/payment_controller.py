from typing import List
from my_project.auth.service.orders.payment_service import PaymentService
from my_project.auth.controller.general_controller import GeneralController


class PaymentController(GeneralController):
    """
    Realisation of Payment controller.
    """
    _service = PaymentService()

    def get_payments_by_user(self, user_id: int) -> List[object]:
        """
        Gets Payment objects from database table filtered by user ID using Service layer as DTO objects.
        :param user_id: ID of the user
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_payments_by_user(user_id)))

    def get_payments_by_reservation(self, reservation_id: int) -> List[object]:
        """
        Gets Payment objects from database table filtered by reservation ID using Service layer as DTO objects.
        :param reservation_id: ID of the reservation
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_payments_by_reservation(reservation_id)))
