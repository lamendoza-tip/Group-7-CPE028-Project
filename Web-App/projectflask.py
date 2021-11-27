from flask import Flask, json, jsonify, request, make_response,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,current_user
from flask import request,render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow



app = Flask(__name__)




## ------------ SQLite Initiallization ------------

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Account.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'TeamJACI123'




## ------------ Flask Login Manager ------------

loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = "login"

@loginmanager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id))




## ------------ SQLite Account database ------------ 

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)

class Account(db.Model,UserMixin):
    __tablename__ = "userlist"
    id = db.Column(db.Integer, primary_key=True)
    email =db.Column(db.String(50))
    fullname = db.Column(db.String(50))
    username = db.Column(db.String(50),unique = True)
    passwd = db.Column(db.String(50))
    

    def __init__(self, email,fullname,username,passwd):
        self.email = email
        self.fullname = fullname
        self.username = username
        self.passwd = passwd
        
class UserSchema(ma.Schema):
	class Meta:
		fields = ("email","fullname","username","passwd")
		
userschema = UserSchema()
usersschemas = UserSchema(many=True)




## ------------ Registration form for registration html ------------ 

class RegisterForm(FlaskForm):
    email= StringField(validators=[InputRequired(),Length(
        min=5, max=50)],render_kw={"placeholder":"Enter your email address"})
    fullname= StringField(validators=[InputRequired(),Length(
        min=5, max=50)],render_kw={"placeholder":"Enter your full name"})
    username= StringField(validators=[InputRequired(),Length(
        min=5, max=50)],render_kw={"placeholder":"Enter your username"})
    passwd= PasswordField(validators=[InputRequired(),Length(
        min=6, max=50)],render_kw={"placeholder":"Enter your password"})

    submit = SubmitField("Register")

    def validate_username(self,username):
        existing_username= Account.query.filter_by(username=username.data).first()

        if existing_username:
            raise ValidationError("Request denied, the username already exist")




## ------------ Login form for login html ------------ 

class LoginForm(FlaskForm):
    username= StringField(validators=[InputRequired(),Length(
        min=5, max=50)],render_kw={"placeholder":"Enter your username"})
    passwd= PasswordField(validators=[InputRequired(),Length(
        min=6, max=50)],render_kw={"placeholder":"Enter your password"})

    submit = SubmitField("Login")




## ------------ Flask app route (html navigation) ------------ 

@app.route("/")
def main():
    return render_template("home.html",name=current_user)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/monitoring")
def monitoring():
    return render_template("monitoring.html")




## ------------ REGISTRATION PART ------------ 

@app.route("/registration", methods = ['GET','POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        encryptpass = bcrypt.generate_password_hash(form.passwd.data)
        add_user = Account(username=form.username.data,passwd= encryptpass,email=form.email.data,fullname= form.fullname.data)
        db.session.add(add_user)
        db.session.commit()
    return render_template("registration.html",form=form)




## ------------ LOGIN PART ------------ 

@app.route("/login", methods = ['GET','POST'] )
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user= Account.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.passwd,form.passwd.data):
                login_user(user)
                return redirect(url_for("main"))
            
            else:
                return "ERROR"
    return render_template("login.html",form=form)


@app.route('/logout', methods = ['GET','POST'])
@login_required
def logout():
        logout_user()
        return redirect(url_for('main'))

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=5050)