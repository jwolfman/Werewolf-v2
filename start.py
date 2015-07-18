import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

DATABASE="/tmp/werewolf.db"
DEBUG=True
SECRET_KEY="dev key"
USERNAME="admin"
PASSWORD="default"

app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_envvar("WEREWOLF_SETTINGS",silent=True)

def connect_db():
    return sqlite3.connect(app.config["database"])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource("schema.sql",mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()

#module level functions
#@app.before_request
def before_request():
    g.db=connect_db()

@app.teardown_request
def teardown_request(exception):
    db=getattr(g,"db",None)
    if db is not None:
        db.close()

@app.route('/')
def start():
    return render_template("home.html")
    return redirect(url_for("home"))

@app.route("/login",methods=["GET","POST"])
def login():
    error=None
    if request.method=="POST":
        if request.form["username"]!=app.config["USERNAME"]:
            error="Invalid username"
        elif request.form["password"]!=app.config["PASSWORD"]:
            error="Invalid password"
        else:
            session["logged_in"]=True
            flash("You were logged in")
            return redirect(url_for("home"))
    return render_template("login.html",error-error)

@app.route("/logout")
def logout():
    session.pop("logged_in",None)
    flash("You were logged out")
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()
