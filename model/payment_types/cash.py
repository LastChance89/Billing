from model.payment_types.payment import Payment


class Cash(Payment):

    def __init__(self, name, amt, location):
        self._location = location
        super().__init__(name, amt)

    def set_location(self, location):
        self._location = location
