from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'thewall')
bcrypt = Bcrypt(app)
app.secret_key = "howmuchwoodcouldawoodchuckchuckifawoodchuckcouldchuckwood"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    if 'id' in session:
        return redirect( 'home/{}'.format(session['id']) )
    else:
        return render_template('/index.html')


@app.route('/register', methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    passwordconf = request.form['passwordconf']
    
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
    if password != passwordconf:
        flash("Passwords must be the same", "password_confirm")
        errors = True

    if errors:
        print errors
        return redirect('/')

    else: 
        hash_pw = bcrypt.generate_password_hash(password)
        query = """INSERT INTO users (email, hash_pw, first_name, last_name, created_at, updated_at)
                            VALUES (:email, :hash_pw, :first_name, :last_name, NOW(), NOW() )  """
        data = { 
                'email': email,
                'hash_pw': hash_pw,
                'first_name': first_name,
                'last_name': last_name,
                }
        mysql.query_db(query, data)
        user = mysql.query_db("SELECT * FROM users WHERE email = :email", {'email': email})
        session['id'] = user[0]['id']
        session['name'] = user[0]['first_name']
        return redirect( 'home/{}'.format(session['id']) )



@app.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']

    if len(email) < 1 or len(password) < 1:
        flash("Fields cannot be empty", "login")

    else: 
        user = mysql.query_db("SELECT * FROM users WHERE email = :email", {'email': email} )
        
        if user:
            if bcrypt.check_password_hash(user[0]['hash_pw'], password):
                session['id'] = user[0]['id']
                session['name'] = user[0]['first_name']
                return redirect( 'home/{}'.format(session['id']) )
            else:
                flash("Please check your password", "login")
        else:
            flash("Please enter a registered email", "login")
    
    return redirect('/')


@app.route('/logout', methods=["POST"])
def logout():
    session.pop('id')
    session.pop('name')
    session.pop('friend')
    return redirect('/')


@app.route('/home/<id>')
def home(id):
    #SET USER FRIEND
    session['friend'] = id
    user = mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': id})
    all_users = mysql.query_db("SELECT id, CONCAT_WS(' ', first_name, last_name) AS username FROM users")
    
    #GET MESSAGES
    query = """SELECT messages.id, messages.message, messages.created_at, messages.from_id,
                CONCAT_WS(' ', CONCAT(UCASE(LEFT(users.first_name, 1)), LCASE(SUBSTRING(users.first_name,2))),
                CONCAT(UCASE(LEFT(users.last_name, 1)), LCASE(SUBSTRING(users.last_name,2)))) AS sender
                FROM messages JOIN users ON messages.from_id = users.id
                WHERE to_id = :id; """
    messages = mysql.query_db(query, { 'id': id} )

    #GET COMMENTS
    query = """SELECT c.id as comment_id, m.id as message_id, c.comment, c.created_at,
                CONCAT_WS(' ', CONCAT(UCASE(LEFT(u.first_name, 1)), LCASE(SUBSTRING(u.first_name,2))),
                CONCAT(UCASE(LEFT(u.last_name, 1)), LCASE(SUBSTRING(u.last_name,2)))) AS sender
                FROM messages as m
                JOIN comments  as c ON c.message_id = m.id
                JOIN users as u ON u.id = c.from_id
                WHERE m.to_id = :id ORDER BY m.id; """
    data = { 'id': id }
    comments = mysql.query_db(query, data)
    return render_template("home.html", session=session, user=user[0], messages=messages, comments=comments, all_users = all_users)


@app.route('/postmessage', methods=['POST'])
def postmessage():
    request.form['message']
    query = """INSERT INTO messages (from_id, to_id, message, created_at, updated_at)
                              VALUES(:from_id, :to_id, :message, NOW(), NOW() ); """
    data = {  'from_id': session['id'],
              'to_id': session['friend'],
              'message': request.form['message']   }
    mysql.query_db(query, data)
    return redirect( 'home/{}'.format(session['friend']) )


@app.route('/postcomment/<id>', methods=['POST'])
def postcomment(id):
    query = """INSERT INTO comments (from_id, message_id, comment, created_at, updated_at)
                              VALUES(:from_id, :message_id, :comment, NOW(), NOW() ); """
    data = {  'from_id': session['id'],
              'message_id': id,
              'comment': request.form['comment']   }
    mysql.query_db(query, data)
    return redirect( 'home/{}'.format(session['friend']) )




app.run(debug=True)