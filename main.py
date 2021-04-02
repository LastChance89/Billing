from payment_factory import PaymentFactory


if __name__ == '__main__':
    factory = PaymentFactory()

    user_input = ["credit","Water", 550, 9000, 123456, "01/11/1111", "9999"]

    credit = factory.create_payment(user_input)

    print(credit.print_payment())
