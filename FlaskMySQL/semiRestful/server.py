from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnection
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnection(app, 'restful')
bcrypt = Bcrypt(app)
app.secret_key = "secretkey"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/users')
def index():
    #MAKE BUTTONS IN TABLE
    users = mysql.query_db("SELECT * FROM users")
    return render_template('users.html', users=users)


@app.route('/users/<id>')
def show(id):
    user = mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': id})
    return render_template("showuser.html", user=user[0])


@app.route('/users/<id>/edit')
def edit(id):
    user = mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': id})
    return render_template("edituser.html", user=user[0])


@app.route('/users/<id>', methods=["POST"])
def update(id):
    name = request.form['full_name']
    email = request.form['email']

    query = """UPDATE users SET full_name = :full_name, email = :email, updated_at = NOW()
                WHERE id = :id;"""
    data = {
            'full_name': name,
            'email': email,
            'id': id
            }
    mysql.query_db(query, data)

    return redirect('/users/{}'.format(id) )


@app.route('/users/new')
def new():
    return render_template("newuser.html")


@app.route('/users/create', methods=["POST"])
def create():
    name = request.form['full_name']
    email = request.form['email']

    query = """INSERT INTO users (full_name, email, created_at, updated_at)
                           VALUES(:name, :email, NOW(), NOW() ); """
    data = { 'name': name, 'email': email }
    mysql.query_db(query, data)

    user = mysql.query_db("SELECT * FROM users WHERE email = :email", {'email': email  } )
    id = user[0]['id']
    return redirect( 'users/{}'.format(id) )


@app.route('/users/<id>/destroy')
def destroy(id):
    mysql.query_db("DELETE FROM users WHERE id = :id;", {'id': id })
    return redirect('/users')





app.run(debug=True)