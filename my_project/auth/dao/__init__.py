"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
#from .orders.client_dao import ClientDAO
#from .orders.client_type_dao import ClientTypeDAO
from .orders.user_dao import UserDAO
from .orders.emailconfirmation_dao import EmailConfirmationDAO
from .orders.room_dao import RoomDAO
from .orders.reservation_dao import ReservationDAO
from .orders.payment_dao import PaymentDAO

#client_dao = ClientDAO()
#client_type_dao = ClientTypeDAO()
user_dao = UserDAO()
emailconfirmation_dao = EmailConfirmationDAO()
payment_dao = PaymentDAO()
room_dao = RoomDAO()
reservation_dao = ReservationDAO()

