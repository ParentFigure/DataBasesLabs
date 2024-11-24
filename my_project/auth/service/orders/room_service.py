from typing import List
from my_project.auth.dao.orders.room_dao import RoomDAO
from my_project.auth.service.general_service import GeneralService


class RoomService(GeneralService):
    """
    Implementation of Room service.
    """
    _dao = RoomDAO()

    def find_by_hotel(self, hotel_id: int) -> List[object]:
        """
        Gets Room objects from the database by hotel ID.
        :param hotel_id: hotel ID value
        :return: list of Room objects
        """
        return self._dao.find_by_hotel(hotel_id)

    def find_available_rooms(self) -> List[object]:
        """
        Gets available Room objects from the database.
        :return: list of available Room objects
        """
        return self._dao.find_available_rooms()
