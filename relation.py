from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from sqlalchemy.orm import joinedload
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/shashi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Post(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(80),nullable=False)
	body=db.Column(db.Text,nullable=False)
	pub_date=db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	category_id=db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
	category=db.relationship('Category',backref=db.backref('posts',lazy=True))
	def __repr__(self):
		return "<Post %r"%self.title
class Category(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),nullable=False)
	def __repr__(self):
		return '<Category %r'%self.name

db.create_all()
py=Category(name='Python')
Post(title='Hello Python!',body='Python is preety cool',category=py)
p=Post(title="Hello Flask!",body="Flask is python framework")
py.posts.append(p)
db.session.add(py)
print(py.posts)
query=Category.query.options(joinedload('posts'))
for category in query:
	print category,category.posts