from flask import redirect, render_template, request, session, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from app import app
from flask import render_template
from db import db
import users
import secrets



@app.route("/")
@app.route("/home")
def index():
    sql = text("SELECT b.*, COALESCE(SUM(v.vote), 0) AS total_votes FROM blogs b LEFT JOIN votes v ON b.id = v.blog_id GROUP BY b.id")
    result = db.session.execute(sql)
    posts = result.fetchall()
    admin = users.is_admin()
    
    return render_template("home.html", posts = posts, admin = admin)

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
            session["csrf_token"] = secrets.token_hex(16)
            return redirect("/")
        else:
            flash("wrong password!")
            return redirect("/")


@app.route("/register",methods=["POST"])
def register():
    username = request.form["username"]
    users.csrf_check()
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
    users.csrf_check()
    sql = text("INSERT INTO blogs (author, title, content, date_posted) VALUES (:author, :title, :content, current_timestamp)")
    db.session.execute(sql, {"author":author, "title":title, "content":content,})
    db.session.commit()
    return redirect("/")

@app.route("/votef", methods=["POST"])
def votef():
    blog_id = request.form.get("blog_id")

    user_id = users.get_userid()
    users.csrf_check()
    
    sql = text(f"select sum(vote) from votes where user_id = {user_id} and blog_id = {blog_id}")
    votes = db.session.execute(sql, {"user_id": user_id, "blog_id": blog_id})
    votes = votes.fetchone()[0]
    if votes != None:
        flash(f"Already voted on this blog {votes}", "error")
        return redirect("/")

    vote_type = request.form.get("vote_type")
    
    if vote_type not in ["upvote", "downvote"]:
        flash("Invalid vote type", "error")
        return redirect("/")
    elif vote_type == "upvote":
        vote_type = 1
    else:
        vote_type = -1
    
    sql = text("INSERT INTO votes (blog_id, user_id, vote) VALUES (:blog_id, :user_id, :vote)")
    db.session.execute(sql, {"blog_id":blog_id, "user_id":user_id, "vote":vote_type})
    db.session.commit()
    
    return redirect("/")


@app.route("/comment/<int:blog_id>")
def comment(blog_id):
    sql = text(f"SELECT * FROM comments WHERE blog_id = {blog_id} ORDER BY date_posted;")
    result = db.session.execute(sql)
    comments = result.fetchall()
    admin = users.is_admin()

    return render_template("comment.html", blog_id=blog_id, comments=comments, admin=admin)

@app.route("/leavecomment", methods=["POST"])
def leavecomment():
    content = request.form.get("teksti")
    username = session["username"]
    blog_id = request.form.get("blog_id")
    user_id = users.get_userid()
    users.csrf_check()

    sql = text("INSERT INTO comments (content, username, blog_id, user_id,  date_posted) VALUES (:content, :username, :blog_id, :user_id, current_timestamp)")
    db.session.execute(sql, {"content":content, "username":username, "blog_id":blog_id, "user_id":user_id})
    db.session.commit()

    return redirect(f"/comment/{blog_id}")

@app.route("/delete", methods=["POST"])   
def delete():
    blog_id = request.form.get("blog_id")
    users.csrf_check()

    sql = text(f"DELETE FROM blogs WHERE id = {blog_id}")
    db.session.execute(sql, {"id":blog_id})
    db.session.commit()

    return redirect("/") 

@app.route("/delete_comment", methods=["POST"])   
def delete_comment():
    comment_id = request.form.get("comment_id")
    blog_id = request.form.get("blog_id")
    users.csrf_check()

    sql = text(f"DELETE FROM comments WHERE id = {comment_id}")
    db.session.execute(sql, {"id":comment_id})
    db.session.commit()

    return redirect(f"/comment/{blog_id}") 

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

