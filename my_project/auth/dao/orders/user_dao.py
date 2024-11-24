from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import User


class UserDAO(GeneralDAO):
    """
    Implementation of User data access layer.
    """
    _domain_type = User

    def find_by_username(self, username: str) -> List[User]:
        return self._session.query(User).filter(User.username == username).all()

    def find_by_email(self, email: str) -> List[User]:
        return self._session.query(User).filter(User.email == email).all()
