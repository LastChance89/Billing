from model.payment_types.cash import Cash
from model.payment_types.check import Check
from model.payment_types.credit import Credit
from model.payment_types.payment import Payment


class PaymentFactory:

    def create_payment(self, user_input):
        if user_input[0] == "credit":
            return Credit(user_input[1], user_input[2], user_input[3], user_input[4], user_input[5], user_input[6])
        elif user_input[0] == "check":
            return Check(user_input[1], user_input[2], user_input[3], user_input[4])
            print("do stuff here eventually")
        elif user_input[0] == "cash":
            return Cash(user_input[1], user_input[2], user_input[3])
            print("do stuff here eventually")
        elif user_input[0] == "payment":
            return Payment(user_input[1], user_input[2])
        else:
            print("Invalid type. Throw an error here.")
