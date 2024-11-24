"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

#from .orders.client_controller import ClientController
#from .orders.client_type_controller import ClientTypeController
from .orders.user_controller import UserController
from .orders.emailconfirmation_controller import EmailConfirmationController
from .orders.room_controller import RoomController
from .orders.reservation_controller import ReservationController
from .orders.payment_controller import PaymentController


#client_controller = ClientController()
#client_type_controller = ClientTypeController()
user_controller = UserController()
email_confirmation_controller = EmailConfirmationController()
room_controller = RoomController()
reservation_controller = ReservationController()
payment_controller = PaymentController()
