from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.emailconfirmation import EmailConfirmation


class EmailConfirmationDAO(GeneralDAO):
    """
    Implementation of EmailConfirmation data access layer.
    """
    _domain_type = EmailConfirmation

    def find_by_user(self, user_id: int) -> List[EmailConfirmation]:
        return self._session.query(EmailConfirmation).filter(EmailConfirmation.user_id == user_id).all()

    def find_by_status(self, status: str) -> List[EmailConfirmation]:
        return self._session.query(EmailConfirmation).filter(EmailConfirmation.confirmation_status == status).all()
