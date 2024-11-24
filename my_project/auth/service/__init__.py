"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

#from .orders.client_service import ClientService
#from .orders.client_type_service import ClientTypeService
from .orders.user_service import UserService
from .orders.emailconfirmation_service import EmailConfirmationService
from .orders.room_service import RoomService
from .orders.reservation_service import ReservationService
from .orders.payment_service import PaymentService

#client_service = ClientService()
#client_type_service = ClientTypeService()
user_service = UserService()
emailconfirmation_service  = EmailConfirmationService()
room_service = RoomService()
reservation_service = ReservationService()
payment_service = PaymentService()


