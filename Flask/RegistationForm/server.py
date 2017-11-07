from flask import Flask, render_template, redirect, request, session, flash
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
app.secret_key = "supercalifragilisticexpialidocious"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def submit():

    errors = False

    if len(request.form['email']) < 1:
        flash("All fields are required", "email")
        errors = True
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address", "email")
        errors = True
        
    if len(request.form['first_name']) < 1:
        flash("All fields are required", "firstname")
        errors = True
    elif request.form['first_name'].isalpha() == False:
        flash("Only letters, no numbers", "firstname")
        errors = True

    if len(request.form['last_name']) < 1:
        flash("All fields are required", "lastname")
        errors = True
    elif request.form['last_name'].isalpha() == False:
        flash("Only letters, no numbers", "lastname")
        errors = True

    try:
        userdate = datetime.datetime.strptime(request.form['date'], '%Y-%m-%d')
        todaydate = datetime.datetime.now()
        mindate = todaydate - datetime.timedelta(days=(18*365))
    except:
        flash("Enter a valid date of birth", "date")
        errors = True
    else:
        if userdate > todaydate:
            flash("Enter a valid date of birth. Must be in the past", "date")
            errors = True
        elif userdate > mindate:
            flash("Enter a valid date of birth. Must be 18 years old", "date")
            errors = True

    
    password = request.form['password']
    numbers = sum(1 for c in password if c.isnumeric())
    upper = sum(1 for c in password if c.isupper())
    
    if len(password) < 1:
        flash("All fields are required", "password")
        errors = True
    else:
        if len(password) < 8:
            flash("Password must be at least 8 characters", "password")
            errors = True
        if numbers < 1 or upper < 1:
            flash("Password must contain at least 1 uppercase and 1 number", "password")
            errors = True
        if request.form['password'] != request.form['confirm_password']:
            flash("Passwords do not match", "confirm")
            errors = True

    
    if errors == False:
        flash("Success!", "success")

    return redirect('/')

app.run(debug=True)