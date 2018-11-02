from flask import Flask
from flask_restful import Resource ,Api
from requests import put, get
from flask import request

app=Flask(__name__)
api=Api(app)

todos = {}

class TodoSimple(Resource):
	def get(self,todo_id):
		print(todos[todo_id])
		return {todo_id:todos[todo_id]}

	def put(self,todo_id):
		todos[todo_id] = request.form['data']
		return {todo_id:todos[todo_id]}


api.add_resource(TodoSimple,'/<string:todo_id>')

if __name__=='__main__':
	app.run(debug=True)
	# put('http://localhost:5000/todo2', data={'data': 'Remember the milk'}).json()
