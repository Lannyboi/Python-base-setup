from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "landon"
    lastname = "Gray"
    return render_template("index.html", name=name, lastname=lastname)

@app.route("/login")
def login():
    return render_template("login.html")
