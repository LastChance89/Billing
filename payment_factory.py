from model.payment_types.cash import Cash
from model.payment_types.check import Check
from model.payment_types.credit import Credit
from model.payment_types.payment import Payment
import json

class PaymentFactory:

    def create_payment(self, user_input):
        user_input = json.loads(user_input)
        if user_input["type"] == "credit":
            return Credit(user_input["name"], user_input["amt"], user_input["credit_max"], user_input["card_no"],user_input["exp_date"],user_input["sec_code"])
        elif user_input["type"] == "check":
            return Check(user_input["name"], user_input["amt"],user_input["acc_num"] ,user_input["routing_num"],user_input["acc_name"])
        elif user_input["type"] == "cash":
            return Cash(user_input["name"], user_input["amt"], user_input["location"])
        elif user_input["type"] == "payment":
            return Payment(user_input["name"], user_input["amt"])
        else:
            print("Invalid type. Throw an error here.")
