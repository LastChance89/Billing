import unittest
from factory.payment_factory import PaymentFactory
from model.payment_types.credit import Credit
from model.payment_types.check import Check
from model.payment_types.cash import Cash
from model.payment_types.payment import Payment


class MyTestCase(unittest.TestCase):

    def test_payment_factory(self):
        payment_factory = PaymentFactory()

        # credit  name, amt, credit_max, card_no, exp_date, sec_code
        user_input = '{"type":"credit", "name":"Water", "amt":550,"credit_max":9000, "card_no":123456, ' \
                     '"exp_date":"01/11/1111", "sec_code":999} '
        credit = payment_factory.create_payment(user_input)
        printed = credit.print_payment()
        self.assertEqual(printed, "Payment for Water in the amount of 550 has been processed. You have used 9000 out "
                                  "of a max of 9000 credit remaining")
        self.assertIsInstance(credit, Credit)

        # check  name, amt, acc_num, routing_num, acc_name)
        user_input = '{"type":"check", "name":"Electric", "amt":550, "acc_num":44444, "routing_num":123456, ' \
                     '"acc_name": "Generic"} '
        check = payment_factory.create_payment(user_input)
        printed = check.print_payment()
        self.assertEqual(printed, "Payment for Electric in the amount of 550 Has been processed for Generic")
        self.assertIsInstance(check, Check)

        # cash  name, amt, location
        user_input = '{"type":"cash", "name":"Food", "amt":550,"location":"Generic Location"}'
        cash = payment_factory.create_payment(user_input)
        printed = cash.print_payment()
        self.assertEqual(printed, "Payment for Food in the amount of 550 Cash Payment setup for location: Generic "
                                  "Location")
        self.assertIsInstance(cash, Cash)

        # payment name, amt
        user_input = '{"type":"payment", "name":"Random", "amt":550} '
        payment = payment_factory.create_payment(user_input)
        printed = payment.print_payment(None)
        self.assertEqual(printed, "Payment for Random in the amount of 550 ")
        self.assertIsInstance(payment, Payment)


if __name__ == '__main__':
    unittest.main()
