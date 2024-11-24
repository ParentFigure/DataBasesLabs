from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.room import Room


class RoomDAO(GeneralDAO):
    """
    Implementation of Room data access layer.
    """
    _domain_type = Room

    def find_by_hotel(self, hotel_id: int) -> List[Room]:
        return self._session.query(Room).filter(Room.hotel_id == hotel_id).all()

    def find_available_rooms(self) -> List[Room]:
        return self._session.query(Room).filter(Room.availability == True).all()
