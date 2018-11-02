from flask import Flask, url_for
from flask import render_template
from flask import Markup
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
    Markup.escape('<blink>hacker</blink>')
    Markup('<em>Marked up</em> &raquo; HTML').striptags()
    return render_template('hello.html', name=name,data=Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')


# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello, World'
# @app.route('/python')
# def python():
#     return 'Shashi love python'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % subpath