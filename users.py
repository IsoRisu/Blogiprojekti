from db import db
from flask import session
from sqlalchemy import text

def get_userid():
    if 'username' in session:
        username = session["username"]
        sql = text(f"SELECT id FROM users WHERE username = '{username}'")
        user_id = db.session.execute(sql, {"username": username})
        user_id = user_id.fetchone()[0]
        return user_id
    else:
        # Handle the case when the 'username' key is not in the session
        return None 

def is_admin():

    user_id = get_userid()
    if user_id == None:
        return False
    
    sql = text(f"SELECT id FROM admins WHERE user_id = '{user_id}'")
    admin_id = db.session.execute(sql, {"user_id": user_id}).fetchone()
    if admin_id is not None:
        return True
    return False

