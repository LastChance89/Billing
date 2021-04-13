from flask import Blueprint
from factory.payment_factory import PaymentFactory

blueprint = Blueprint('payment', __name__)


@blueprint.route('/payment/create', methods=('POST',))
def create_payment():
    print("BLEH")
