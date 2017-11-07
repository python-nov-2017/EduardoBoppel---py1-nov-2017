from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "verysecretkeythatnooneknowsshhhhhhhh"



@app.route('/')
def index():
    try:
        session['generate'] += 1
    except:
        session['generate'] = 1
        
    if session['generate'] == 1:
        session['number'] = random.randrange(0, 101)
        session['guess'] = ""
        session['message'] = ""

    return render_template("index.html", guess=session['guess'], val=session["message"], btnvalue="Guess")



@app.route('/guess', methods=["POST"])
def guess():   
    try:
        session['guess'] = int(request.form['guess'])
    except:
        return redirect('/')
    
    else:
        if session['guess'] > session['number']:
            session["message"] = "It is too high"
        elif session['guess'] < session['number']:
            session["message"] = "It is too low"
        elif session['guess'] == session['number']:
            session["message"] = "You got it!"
            session['generate'] = 0
            return render_template("index.html", val=session["message"], btnvalue="Play Again")
        else:
            session["message"] = "Pick only a number!"

        return redirect('/')




app.run(debug=True)