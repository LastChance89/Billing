from model.payment_types.payment import Payment


class Cash(Payment):

    def __init__(self, name, amt, location):
        self._location = location
        super().__init__(name, amt)

    def set_location(self, location):
        self._location = location

    def get_location(self):
        return self._location

    def print_payment(self):
        custom_data = "Cash Payment setup for location: " + self.get_location()
        return super().print_payment(custom_data)

