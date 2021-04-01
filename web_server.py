from flask import Flask, render_template,request
import mysql.connector
app =Flask('FlaskWork', template_folder='./templates')

@app.route('/')
def index():
    return render_template('/index.html')




if __name__ == '__main__':


    app.run()