from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "specialverysecretkey"

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']

    if len(name) > 0 and len(comment) > 0 and len(comment) < 120:
        print "ok"
        return render_template("success.html", name=name, location=location, language=language, comment=comment)
    
    else:
        if len(name) < 1:
            print "name error"
            flash("Name cannot be empty")
        if len(comment) < 1:
            print "comment short"
            flash("Comment cannot be empty")
        if len(comment) > 120:
            print "comment long"
            flash("Comment cannot be larger than 120 characters")
        return redirect ('/')


app.run(debug=True)