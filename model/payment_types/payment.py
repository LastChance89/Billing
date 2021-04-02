class Payment:
    def __init__(self, name, amt):
        self._name = name
        self._amt = amt

    def set_name(self, name):
        self._name = name

    def set_amt(self, amt):
        self._amt = amt

    def get_amt(self):
        return self._amt

    def get_name(self):
        return self._name

    def print_payment(self, custom_data):
        return "Payment for " + self.get_name() + " in the amount of " + str(self.get_amt()) + " " + custom_data
