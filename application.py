from flask import Flask
application= Flask(__name__)

@application.route('/')
def hello_world():
    return render_template('index.html')
@application.route('/login')
def login():   
    """
    This method is called for login
    """
    return render_template('login.html')
