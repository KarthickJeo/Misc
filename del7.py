from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONOGO_DBNAME'] = 'accion_sales_db'
app.config['MONGO_URI'] = 'mongodb://jikarthi:Accion123@ds127878.mlab.com:27878/accion_sales_db'

mongo = PyMongo(app)

@app.route('/add')
def add ():
    user = mongo.db.users
    user.insert({'name' : 'Karthick'})
    return 'User is added'

if __name__ == ('__main__'):
    app.run(debug = True)
