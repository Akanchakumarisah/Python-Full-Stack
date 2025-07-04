from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "HELLO WORLD"

@app.route("/about")
def about():
    return "This is about"

@app.route("/contact")
def contact():
    return "Contact Us"

@app.route("/user/<name>")
def user(name):
    return render_template("index.html", name=name)