from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
app.secret_key = 'newenglandclamchowder'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=friends)


@app.route('/friends', methods=["POST"])
def create():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    
    # check to see if any values are empty
    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1:
        flash("Fields cannot be empty", 'form-error')
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email address", 'form-error')
    else:    
        query = "INSERT INTO friends (first_name, last_name, email) VALUES (:first_name, :last_name, :email);"
        data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email
                }
        mysql.query_db(query, data)
        flash("Friend successfully added", 'form-success')
    
    return redirect ('/')


@app.route('/friends/<id>/edit', methods=["GET"])
def edit(id):
    query = "SELECT * FROM friends WHERE id = :id"
    data = { 'id': id }
    friend = mysql.query_db(query, data)
    return render_template ('edit.html', friend=friend[0])


@app.route('/friends/<id>', methods=["GET", "POST"])
def update(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    if len(first_name) < 1 or len(last_name) < 1 or len(email) < 1:
        flash("Fields cannot be empty", 'form-error')
    elif not EMAIL_REGEX.match(email):
        flash("Please enter a valid email address", 'form-error')
    else:
        query = """ UPDATE friends SET
                    first_name = :first_name,
                    last_name = :last_name,
                    email = :email,
                    updated_at = NOW()
                    WHERE id = :id ; """
        data = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'id': id
                }
        mysql.query_db(query, data)
        flash('Friend sucessfully updated', 'table')
        return redirect ('/')
    url = '/friends/{}'.format(id)
    print url
    return redirect ('/friends/{}/edit'.format(id))



@app.route('/friends/<id>/delete', methods=["POST"])
def destroy(id):
    query = " DELETE FROM friends WHERE id = :id ; "
    data = { 'id': id }
    mysql.query_db(query, data)
    flash('Friend sucessfully deleted', 'table')
    return redirect ('/')



app.run(debug=True)