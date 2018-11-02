from flask import Flask
from flask_restful import Resource ,Api
db=SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://localhost/root/root/shashi'

# db = MySQLdb.connect("localhost","root","root","shashi" )
# cursor = db.cursor()
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    empname = Col('Empname')
    empid = Col('Empid')
    deviceid = Col('Deviceid')

# Get some objects
class Item(object):
    def __init__(self, empname, empid,deviceid):
        self.empname = empname
        self.empid = empid
        self.deviceid = deviceid

items = [Item('shash_1', '11','linux11'),
         Item('shash_2', '12','linux12'),
         Item('shash_3', '13','linux13')]
# Or, equivalently, some dicts
items = [dict(empname='shash_1', empid='11', deviceid='linux11'),
         dict(empname='shash_2', empid='12', deviceid='linux12'),
         dict(empname='shash_3', empid='13', deviceid='linux13')]

# Or, more likely, load items from your database with something like
items = ItemModel.query.all()

# Populate the table
table = ItemTable(items)

# Print the html
print(table.__html__())
app=Flask(__name__)
api=Api(app)

class Employee(Resource):
	def get(self):
		return {'Empoyee':'shashi'}
		db.execute("CREATE TABLE minance (empid INT AUTO_INCREMENT PRIMARY KEY, empname VARCHAR(255), deviceid VARCHAR(255))")
		# cursor.execute("INSERT INTO 'minance'('empid','empname','deviceid') VALUES(%s,%s,%s)",(22,'shashi','linux12'))


api.add_resource(Employee,'/')

class Device(Resource):
	def get(self):
		return {'device':'linux12'}

api.add_resource(Device,'/device')

if __name__=='__main__':
	app.run(debug=True)
