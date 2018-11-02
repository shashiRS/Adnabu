from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/shashi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	username=db.Column(db.String(100),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	def __repr__(self):
	 	return '<User %r>' %self.username

db.create_all()

admin=User(username='shash1',email='shashi1@example.com')
guest=User(username='hemsz1',email='hemsz1@example.com')

db.session.add(admin)
db.session.add(guest)
db.session.commit()
print(User.query.all())
print(User.query.filter_by(username='admin').first())