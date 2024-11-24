from typing import List
from my_project.auth.dao.orders.emailconfirmation_dao import EmailConfirmationDAO
from my_project.auth.service.general_service import GeneralService


class EmailConfirmationService(GeneralService):
    """
    Implementation of EmailConfirmation service.
    """
    _dao = EmailConfirmationDAO()

    def find_by_user(self, user_id: int) -> List[object]:
        """
        Gets EmailConfirmation objects from the database by user ID.
        :param user_id: user ID value
        :return: list of EmailConfirmation objects
        """
        return self._dao.find_by_user(user_id)

    def find_by_status(self, status: str) -> List[object]:
        """
        Gets EmailConfirmation objects from the database by status.
        :param status: status value
        :return: list of EmailConfirmation objects
        """
        return self._dao.find_by_status(status)
