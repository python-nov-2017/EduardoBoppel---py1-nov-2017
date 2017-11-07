from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "secretkey"


@app.route('/')
def index():
    session['visits'] += 1
    return render_template("index.html")

@app.route('/add', methods=["POST"])
def add():
    session['visits'] += 1
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['visits'] = 0
    return redirect ('/')

app.run(debug=True)