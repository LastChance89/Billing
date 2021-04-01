from model.payment_types.payment import Payment


class Credit(Payment):

    def __init__(self, name, amt, credit_max, card_no, exp_date, sec_code):
        self._credit_max = credit_max
        self._card_no = card_no
        self._exp_date = exp_date
        self._sec_code = sec_code
        super().__init__(name, amt)

    def set_credit_max(self, credit_max):
        self._credit_max = credit_max

    def get_credit_max(self):
        return self._credit_max

    def print_payment(self):
        print("Credit info " + super().print_payment() + " " + str(self.get_credit_max()))