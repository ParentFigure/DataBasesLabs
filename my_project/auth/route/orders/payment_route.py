from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller.orders.payment_controller import PaymentController
from my_project.auth.domain.orders.payment import Payment

payment_bp = Blueprint('payments', __name__, url_prefix='/payments')
payment_controller = PaymentController()

@payment_bp.get('')
def get_all_payments() -> Response:
    return make_response(jsonify(payment_controller.find_all()), HTTPStatus.OK)

@payment_bp.post('')
def create_payment() -> Response:
    content = request.get_json()
    payment = Payment.create_from_dto(content)
    payment_controller.create(payment)
    return make_response(jsonify(payment.put_into_dto()), HTTPStatus.CREATED)

@payment_bp.get('/<int:payment_id>')
def get_payment(payment_id: int) -> Response:
    return make_response(jsonify(payment_controller.find_by_id(payment_id)), HTTPStatus.OK)

@payment_bp.get('/user/<int:user_id>')
def get_payments_by_user(user_id: int) -> Response:
    return make_response(jsonify(payment_controller.get_payments_by_user(user_id)), HTTPStatus.OK)

@payment_bp.delete('/<int:payment_id>')
def delete_payment(payment_id: int) -> Response:
    payment_controller.delete(payment_id)
    return make_response("Payment deleted", HTTPStatus.OK)
