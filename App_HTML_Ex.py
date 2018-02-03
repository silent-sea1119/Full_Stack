
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('login2.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		#session['logged_in'] = True
		return 'True'
	else:
		flash('wrong password!')
		return 'fail'


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(host = '127.0.0.1', port = 8093 , debug = 'true')
