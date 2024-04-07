from flask import Flask
from flask import redirect, render_template, request, session, flash
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text


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
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cerfkris"
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")


@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts = posts)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        flash("wrong username!")
        return redirect("/")
    else:
        hash_value = user.password
        if check_password_hash(hash_value, password):
            session["username"] = username
            wrong = ""
            return redirect("/")
        else:
            flash("wrong password!")
            return redirect("/")

@app.route("/register",methods=["POST"])
def register():
    username = request.form["username"]
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()    
    if not user:
        password = request.form["password"]
        hash_value = generate_password_hash(password)
        sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
        db.session.execute(sql, {"username":username, "password":hash_value})
        db.session.commit()
    else:
        flash("Username taken")
    
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")