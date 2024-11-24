from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.reservation_controller import ReservationController
from my_project.auth.domain.orders.reservation import Reservation

reservation_bp = Blueprint('reservations', __name__, url_prefix='/reservations')
reservation_controller = ReservationController()

@reservation_bp.get('')
def get_all_reservations() -> Response:
    return make_response(jsonify(reservation_controller.find_all()), HTTPStatus.OK)

@reservation_bp.post('')
def create_reservation() -> Response:
    content = request.get_json()
    reservation = Reservation.create_from_dto(content)
    reservation_controller.create(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)

@reservation_bp.get('/<int:reservation_id>')
def get_reservation(reservation_id: int) -> Response:
    return make_response(jsonify(reservation_controller.find_by_id(reservation_id)), HTTPStatus.OK)

@reservation_bp.get('/user/<int:user_id>')
def get_reservations_by_user(user_id: int) -> Response:
    return make_response(jsonify(reservation_controller.get_reservations_by_user(user_id)), HTTPStatus.OK)

@reservation_bp.get('/room/<int:room_id>')
def get_reservations_by_room(room_id: int) -> Response:
    return make_response(jsonify(reservation_controller.get_reservations_by_room(room_id)), HTTPStatus.OK)

@reservation_bp.delete('/<int:reservation_id>')
def delete_reservation(reservation_id: int) -> Response:
    reservation_controller.delete(reservation_id)
    return make_response("Reservation deleted", HTTPStatus.OK)
