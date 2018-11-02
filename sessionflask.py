from flask import Flask, url_for,redirect
from flask import render_template
from flask import request
import re
from flask import Flask, session, redirect, url_for, escape, request, flash

app = Flask(__name__)
app.secret_key = b'shashi'

    # @app.route('/')
    # def index():
    #     print(session)
    #     if 'username' in session:
    #         return 'Logged in as %s' % escape(session['username'])
    #     return 'You are not logged in'

    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     if request.method == 'POST':
    #         session['username'] = request.form['username']
    #         return redirect(url_for('index'))
    #     return '''
    #         <form method="post">
    #             <p>Enter User name:<input type=text name=username>
    #             <p><input type=submit value=Login>
    #         </form>
    #     '''

    # @app.route('/logout')
    # def logout():
    #     # remove the username from the session if it's there
    #     session.pop('username', None)
    #     return redirect(url_for('index'))   
@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
                   "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    # print(request.form['username'])
    return '''

    <form action = "" method = "post">
       <p><input type = text name = "username"/></p>
       <p><input type = submit value = "Login"/></p>
    </form>
    
    '''
@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))