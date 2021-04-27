from flask import Blueprint
from service import paymentService
from flask import request

blueprint = Blueprint('payment', __name__)


@blueprint.route('/payment/create', methods=('POST',))
def create_payment():
    data = request.get_json()
    return paymentService.create_payment(data)

