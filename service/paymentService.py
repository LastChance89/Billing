from factory.payment_factory import PaymentFactory

#not sure this is proper python way.
factory = PaymentFactory()
import json
def create_payment(data):
    payment = factory.create_payment(data);

    return json.dumps(payment)