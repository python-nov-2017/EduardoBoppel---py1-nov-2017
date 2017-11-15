from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
bcrypt = Bcrypt(app)
app.secret_key = "cowabunga"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    if "id" in session:
        print "YES session"
        return redirect('/home')
    else:
        print "NO session"
        print session
        return render_template('index.html')    


@app.route('/register', methods=["POST"])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    password_conf = request.form['password_conf']
    errors = False

    if len(first_name) < 2:
        flash("First name must be at least 2 characters", "first_name")
        errors = True
    elif first_name.isalpha() == False:
        flash("First Name can only contain letters", "first_name")
        errors = True

    if len(last_name) < 2:
        flash("Last name must be at least 2 characters", "last_name")
        errors = True
    elif last_name.isalpha() == False:
        flash("Last Name can only contain letters", "last_name")
        errors = True

    if len(email) < 1:
        flash("Email cannot be empty", "email")
        errors = True
    elif not EMAIL_REGEX.match(email):
        flash("Must enter valid email", "email")
        errors = True

    if len(password) < 8:
        flash("Password must be at least 8 characters", "password")
        errors = True
    if password != password_conf:
        flash("Passwords must be the same", "password_confirm")
        errors = True

    if errors:
        return redirect('/')
    
    else:
        pw_hash = bcrypt.generate_password_hash(password)
        query = """INSERT INTO friends (first_name, last_name, email, pw_hash, created_at, updated_at) 
                                VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW() ) """
        data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'pw_hash': pw_hash,
                }
        mysql.query_db(query, data)
        
        user = mysql.query_db("SELECT * FROM friends WHERE email = :email", {'email': email} )
        session['id'] = user[0]['id']
        session['name'] = "{} {}".format(user[0]['first_name'], user[0]['last_name'])
        return redirect('/home')


@app.route('/login', methods=["POST"])
def login():

    email = request.form['email']
    password = request.form['password']

    if len(email) < 1 or len(password) < 1:
        flash("Fields cannot be empty", "login")

    else:
        query = "SELECT * FROM friends WHERE email = :email LIMIT 1"
        data = {'email': email }
        user = mysql.query_db(query, data)
        
        if user:
            if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                session['id'] = user[0]['id']
                session['name'] = "{} {}".format(user[0]['first_name'], user[0]['last_name'])
                return redirect('/home')
            else: 
                flash("Please enter a valid password", "login")
        else: 
            flash("Please enter a valid username", "login")
    
    return redirect('/')



@app.route('/logout', methods=["POST"])
def logout():
    session.pop('id')
    session.pop('name')
    return redirect('/')


@app.route('/home')
def home():
    return render_template('home.html', user=session)




app.run(debug=True)
