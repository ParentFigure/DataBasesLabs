from typing import List
from my_project.auth.service.orders.user_service import UserService
from my_project.auth.controller.general_controller import GeneralController


class UserController(GeneralController):
    """
    Realisation of User controller.
    """
    _service = UserService()

    def get_users_by_email(self, email: str) -> List[object]:
        """
        Gets User objects from database table filtered by email using Service layer as DTO objects.
        :param email: email value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_users_by_email(email)))

    def get_users_by_role(self, role: str) -> List[object]:
        """
        Gets User objects from database table filtered by role using Service layer as DTO objects.
        :param role: role value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_users_by_role(role)))
