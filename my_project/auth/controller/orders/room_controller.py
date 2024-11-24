from typing import List
from my_project.auth.service.orders.room_service import RoomService
from my_project.auth.controller.general_controller import GeneralController


class RoomController(GeneralController):
    """
    Realisation of Room controller.
    """
    _service = RoomService()

    def get_rooms_by_capacity(self, capacity: int) -> List[object]:
        """
        Gets Room objects from database table filtered by capacity using Service layer as DTO objects.
        :param capacity: capacity value
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_rooms_by_capacity(capacity)))

    def get_rooms_by_type(self, room_type: str) -> List[object]:
        """
        Gets Room objects from database table filtered by type using Service layer as DTO objects.
        :param room_type: type of room
        :return: list of all objects as DTOs
        """
        return list(map(lambda x: dict(x), self._service.get_rooms_by_type(room_type)))
