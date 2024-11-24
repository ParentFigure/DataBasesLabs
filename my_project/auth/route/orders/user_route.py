from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.user_controller import UserController
from my_project.auth.domain.orders.user import User

user_bp = Blueprint('users', __name__, url_prefix='/users')
user_controller = UserController()

@user_bp.get('')
def get_all_users() -> Response:
    return make_response(jsonify(user_controller.find_all()), HTTPStatus.OK)

@user_bp.post('')
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    return make_response(jsonify(user_controller.find_by_id(user_id)), HTTPStatus.OK)

@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update(user_id, user)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)

@user_bp.get('/email/<string:email>')
def get_users_by_email(email: str) -> Response:
    return make_response(jsonify(user_controller.get_users_by_email(email)), HTTPStatus.OK)

@user_bp.get('/role/<string:role>')
def get_users_by_role(role: str) -> Response:
    return make_response(jsonify(user_controller.get_users_by_role(role)), HTTPStatus.OK)

