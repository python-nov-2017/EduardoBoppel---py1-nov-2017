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
        session['log'] = []

    return render_template("index.html", amount=session['gold'], log=session['log'])



@app.route('/process_money', methods=["POST"])
def process_money():
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if request.form['building'] == "farm":    
        goldwon = random.randint(10, 20)
        session['log'].append( {'result': "Won {} golds in the farm".format(goldwon), 'class': "win", 'time': time} )
       
    elif request.form['building'] == "cave":
        goldwon = random.randint(5, 10)
        session['log'].append( {'result': "Won {} golds in the cave".format(goldwon), 'class': "win", 'time': time} )
       
    elif request.form['building'] == "house":
        goldwon = random.randint(2, 5)
        session['log'].append( {'result': "Won {} golds in the house".format(goldwon), 'class': "win", 'time': time} )
       
    else:
        goldwon = random.randrange(-50, 50)
        if goldwon >= 0:
            session['log'].append( {'result': "Won {} golds in the house".format(goldwon), 'class': "win", 'time': time} )
        else:
            session['log'].append( {'result': "Lost {} golds in the house".format(goldwon), 'class': "lose", 'time': time} )
        
    session['gold'] += goldwon
    return redirect('/')


@app.route('/reset')
def reset():
    session.pop('gold')
    session.pop('log')
    return redirect('/')



app.run(debug=True)