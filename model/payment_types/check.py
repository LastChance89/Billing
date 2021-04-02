from model.payment_types.payment import Payment


class Check(Payment):

    def __init__(self, name, amt, acc_num, routing_num, acc_name):
        self._acc_num = acc_num
        self._routing_num = routing_num
        self._acc_name = acc_name
        super().__init__(name, amt)

    def set_acc_name(self, acc_name):
        self._acc_num = acc_name

    def set_acc_um(self, acc_num):
        self._acc_num = acc_num

    def set_routing_num(self,rounting_num):
        self._routing_num = rounting_num

    def get_acc_name(self):
        return self._acc_name

    def print_payment(self):
        custom_data = "Has been processed for " + self.get_acc_name()
        return super().print_payment(custom_data)