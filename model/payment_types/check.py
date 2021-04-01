from model.payment_types.payment import Payment


class Check(Payment):

    def __init__(self, name, amt, acc_num, routing_num):
        self._acc_num = acc_num
        self._routing_num = routing_num
        super.__init__(name, amt)
