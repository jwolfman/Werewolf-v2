from flask import Flask, url_for;
from app import app;

@app.route('/home')
def homePage():
	return render_template('home.html');
	
@app.route('/login')
def loginPage():
	return render_template('login.html');
	
@app.route('/moderator')
def moderatorPage():
	return render_template('moderator.html');
