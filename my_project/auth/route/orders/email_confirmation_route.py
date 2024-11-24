from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.emailconfirmation_controller import EmailConfirmationController

emailconfirmation_bp = Blueprint('emailconfirmations', __name__, url_prefix='/emailconfirmations')
emailconfirmation_controller = EmailConfirmationController()

@emailconfirmation_bp.get('')
def get_all_email_confirmations() -> Response:
    return make_response(jsonify(emailconfirmation_controller.find_all()), HTTPStatus.OK)

@emailconfirmation_bp.get('/user/<int:user_id>')
def get_confirmations_by_user(user_id: int) -> Response:
    return make_response(jsonify(emailconfirmation_controller.get_confirmations_by_user(user_id)), HTTPStatus.OK)

@emailconfirmation_bp.get('/pending')
def get_pending_confirmations() -> Response:
    return make_response(jsonify(emailconfirmation_controller.get_pending_confirmations()), HTTPStatus.OK)
