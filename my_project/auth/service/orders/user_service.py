from typing import List
from my_project.auth.dao.orders.user_dao import UserDAO
from my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    """
    Implementation of User service.
    """
    _dao = UserDAO()

    def find_by_username(self, username: str) -> List[object]:
        """
        Gets User objects from the database by username.
        :param username: username value
        :return: list of User objects
        """
        return self._dao.find_by_username(username)

    def find_by_email(self, email: str) -> List[object]:
        """
        Gets User objects from the database by email.
        :param email: email value
        :return: list of User objects
        """
        return self._dao.find_by_email(email)
