from flask import Flask, render_template,request
from factory.payment_factory import PaymentFactory
app =Flask('FlaskWork', template_folder='./templates/html')
from controller.payment_controller import blueprint
factory = PaymentFactory()


@app.route('/')
def index():
    return render_template('/index.html')



@app.route('/createPayment', methods = ['post'])
def createPayment():
    print("BLEH")
    #request.form.get('')
    #factory.create_payment(None)

def regester_endpoints():
    app.register_blueprint(blueprint)


if __name__ == '__main__':
    regester_endpoints()
    app.run()


