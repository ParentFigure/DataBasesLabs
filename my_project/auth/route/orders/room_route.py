from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.room_controller import RoomController
from my_project.auth.domain.orders.room import Room

room_bp = Blueprint('rooms', __name__, url_prefix='/rooms')
room_controller = RoomController()

@room_bp.get('')
def get_all_rooms() -> Response:
    return make_response(jsonify(room_controller.find_all()), HTTPStatus.OK)

@room_bp.post('')
def create_room() -> Response:
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.create(room)
    return make_response(jsonify(room.put_into_dto()), HTTPStatus.CREATED)

@room_bp.get('/<int:room_id>')
def get_room(room_id: int) -> Response:
    return make_response(jsonify(room_controller.find_by_id(room_id)), HTTPStatus.OK)

@room_bp.get('/capacity/<int:capacity>')
def get_rooms_by_capacity(capacity: int) -> Response:
    return make_response(jsonify(room_controller.get_rooms_by_capacity(capacity)), HTTPStatus.OK)

@room_bp.get('/type/<string:room_type>')
def get_rooms_by_type(room_type: str) -> Response:
    return make_response(jsonify(room_controller.get_rooms_by_type(room_type)), HTTPStatus.OK)

@room_bp.put('/<int:room_id>')
def update_room(room_id: int) -> Response:
    content = request.get_json()
    room = Room.create_from_dto(content)
    room_controller.update(room_id, room)
    return make_response("Room updated", HTTPStatus.OK)

@room_bp.delete('/<int:room_id>')
def delete_room(room_id: int) -> Response:
    room_controller.delete(room_id)
    return make_response("Room deleted", HTTPStatus.OK)
