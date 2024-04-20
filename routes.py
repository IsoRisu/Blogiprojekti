from flask import redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import datetime
from app import app
from flask import render_template

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///"
db = SQLAlchemy(app)

@app.route("/")
@app.route("/home")
def index():
    sql = text("SELECT author, title, content, date_posted FROM blogs ORDER BY id DESC")
    result = db.session.execute(sql)
    posts = result.fetchall()
    
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

@app.route("/blog",methods=["POST"])
def blog():
    author = session["username"]
    title = request.form["otsikko"]
    content = request.form["teksti"]
    sql = text("INSERT INTO blogs (author, title, content) VALUES (:author, :title, :content)")
    db.session.execute(sql, {"author":author, "title":title, "content":content,})
    db.session.commit()
    return redirect("/")
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

