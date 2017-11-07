from flask import Flask, render_template, redirect, request, session
import random
import datetime
app = Flask(__name__)
app.secret_key = "averymisteriouskey"

@app.route('/')
def index():
    if "gold" not in session:
        session['gold'] = 0
    if "log" not in session:
        session['log'] = "Started your gold search\n"

    return render_template("index.html", amount=session['gold'], log=session['log'])



@app.route('/process_money', methods=["POST"])
def process_money():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if request.form['building'] == "farm":    
        goldwon = random.randint(10, 20)
        session['gold'] += goldwon
        session['log'] = "\t{}: Won {} golds in the farm\n".format(time, goldwon) + session['log']
        
    elif request.form['building'] == "cave":
        goldwon = random.randint(5, 10)
        session['gold'] += goldwon
        session['log'] = "\t{}: Won {} golds in the cave\n".format(time, goldwon) + session['log']
        
    elif request.form['building'] == "house":
        goldwon = random.randint(2, 5)
        session['gold'] += goldwon
        session['log'] = "\t{}: Won {} golds in the house\n".format(time, goldwon) + session['log']
    else:
        goldwon = random.randint(0, 50)
        earnlose = random.random()
        if earnlose >= 0.5:
            session['gold'] += goldwon
            session['log'] = "\t{}: Won {} golds in the casino\n".format(time, goldwon) + session['log']
        else:
            session['gold'] -= goldwon
            session['log'] = "\t{}: Lost {} golds in the casino\n".format(time, goldwon) + session['log']
        
        
    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('log')
    return redirect('/')



app.run(debug=True)