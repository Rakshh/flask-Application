from flask import Flask, render_template, request
application= Flask(__name__)

@application.route('/')
def hello_world():
    return 'hello'
@application.route('/login')
def login():   
    """
    This method is called for login
    """
    return render_template('login.html')
