from flask import Flask, jsonify, request,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlite3
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Account.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'TeamJACI123'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Account(db.Model):
    __tablename__ = "userlist"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    email =db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(50),unique = True)
    passwd = db.Column(db.String(50))
    

    def __init__(self, id,email,fullname,username,passwd):
        self.id = id
        self.email = email
        self.fullname = fullname
        self.username = username
        self.passwd = passwd
        
class UserSchema(ma.Schema):
	class Meta:
		fields = ("id","email","fullname","username","passwd")
		
userschema = UserSchema()
usersschemas = UserSchema(many=True)

@app.route("/users", methods = ['GET','POST'])
def add_user():
    id = request.json.get('id')
    username = request.json.get('username')
    passwd = request.json.get('passwd')
    email = request.json.get('email')
    fullname = request.json.get('fullname')
    add_user = Account(id,username,passwd,email,fullname)
    db.session.add(add_user)
    db.session.commit()
    return userschema.jsonify(add_user)


    #========================================================
    
@app.route('/users', methods=['GET'])
def read_all():
    accounts = Account.query.all()
    result = usersschemas.dump(accounts)
    return usersschemas.jsonify(result).data

@app.route('/users/<id>', methods=['GET'])
def read_user(id):
    user = Account.query.get(id)
    result = userschema.dump(user)
    return userschema.jsonify(result)

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user = Account.query.get(id)

    id = request.json.get('id')
    username = request.json.get('username')
    passwd = request.json.get('passwd')
    email = request.json.get('email')
    fullname = request.json.get('fullname')

    user.username = username
    user.email = email
    user.fullname = fullname

    db.session.commit()
    return userschema.jsonify(user)

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = Account.query.get(student_id)
    db.session.delete(user)
    db.session.commit()
    return userschema.jsonify(user)

if __name__== "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5051, debug=True)

