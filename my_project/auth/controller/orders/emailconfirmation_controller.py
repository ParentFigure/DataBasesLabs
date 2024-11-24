from typing import List
from my_project.auth.service.orders.emailconfirmation_service import EmailConfirmationService
from my_project.auth.controller.general_controller import GeneralController


class EmailConfirmationController(GeneralController):
    """
    Realisation of EmailConfirmation controller.
    """
    _service = EmailConfirmationService()

    def get_confirmations_by_user(self, user_id: int) -> List[object]:
        """
        Gets EmailConfirmation objects from database table filtered by user ID using Service layer as DTO objects.
        :param user_id: ID of the user
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_confirmations_by_user(user_id)))

    def get_pending_confirmations(self) -> List[object]:
        """
        Gets all pending EmailConfirmation objects using Service layer as DTO objects.
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_pending_confirmations()))
