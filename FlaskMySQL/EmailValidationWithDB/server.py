from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app, 'emails')

app.secret_key = "sicretki"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/display')
def display():
    query = "SELECT id, email, created_at FROM emails"
    emails = mysql.query_db(query)
    print session['newemail']
    return render_template('success.html', emails=emails)

@app.route('/add', methods=['POST'])
def add():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email")
    else:
        query = "INSERT INTO emails (email, created_at, update_at) VALUES (:email, NOW(), NOW())"
        data = { 'email': request.form['email'] } 
        mysql.query_db(query, data)
        flash("The email you entered {} is valid!  Thank you!".format(data['email']))
        return redirect('/display')
    return redirect('/')

@app.route('/delete', methods=["POST"])
def delete():
    query = "DELETE FROM emails WHERE id = :id"
    data = { 'id': request.form['id'] } 
    mysql.query_db(query, data)
    flash("Email address sucessfully deleted")
    return redirect('/display')



app.run(debug=True)