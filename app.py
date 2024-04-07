from flask import Flask
from flask import redirect, render_template, request, session
from os import getenv


posts = [
    {   "author": "Risu",
        "title": "Ensimmainen blogini",
        "content": "Tama on ensimmainen kirjoitukseni.",
        "date_posted": "7.4.2024"
    },
    {   "author": "Kisu",
        "title": "Hellurei",
        "content": "Moi kaikille.",
        "date_posted": "6.4.2024"
    }
]

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html", title = "About")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    #check username and password
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")