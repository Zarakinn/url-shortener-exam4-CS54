from flask import Flask, render_template,request,redirect


app = Flask(__name__)

@app.route("/status")
def index():
    return 'Up and running'

@app.route("/display")
def display():
    data = [ 
    ('https://telecomnancy.univ-lorraine.fr/', 'tn', 42), 
    ('https://gitlab.telecomnancy.univ-lorraine.fr/', 'gitlab', 666) 
    ]

    return render_template("display.html",liste = data)