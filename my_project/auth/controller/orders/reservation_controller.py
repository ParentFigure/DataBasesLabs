from typing import List
from my_project.auth.service.orders.reservation_service import ReservationService
from my_project.auth.controller.general_controller import GeneralController


class ReservationController(GeneralController):
    """
    Realisation of Reservation controller.
    """
    _service = ReservationService()

    def get_reservations_by_user(self, user_id: int) -> List[object]:
        """
        Gets Reservation objects from database table filtered by user ID using Service layer as DTO objects.
        :param user_id: ID of the user
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reservations_by_user(user_id)))

    def get_reservations_by_room(self, room_id: int) -> List[object]:
        """
        Gets Reservation objects from database table filtered by room ID using Service layer as DTO objects.
        :param room_id: ID of the room
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_reservations_by_room(room_id)))
