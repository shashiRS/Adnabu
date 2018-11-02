from flask import Flask, url_for,redirect
from flask import render_template
from flask import request
import re
app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/home')
def home():
    return 'Successfully logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("")
    error = None
    if request.method == 'POST':
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", request.form['username']) != None:
            return redirect(url_for('home'))
        else:
            error = 'Invalid Credentials. Please try again.'
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
        #     error = 'Invalid Credentials. Please try again.'
        # else:
        #     return redirect(url_for('home'))
    return render_template('login.html', error=error)