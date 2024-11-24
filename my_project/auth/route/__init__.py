"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    #from .orders.client_route import client_bp
    #from .orders.client_type_route import client_type_bp
    from .orders.user_route import user_bp
    from .orders.room_route import room_bp
    from .orders.payment_route import payment_bp
    from .orders.reservation_route import reservation_bp
    from .orders.email_confirmation_route import emailconfirmation_bp

    #app.register_blueprint(client_bp)
    #app.register_blueprint(client_type_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(room_bp)
    app.register_blueprint(reservation_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(emailconfirmation_bp)
