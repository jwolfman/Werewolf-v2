import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

#DATABASE=""
DEBUG=True
#SECRET_KEY=""

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("Werewolf_settings",silent=True)

def connect_db():
    return sqlite3.connect(app.config["database"])

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
