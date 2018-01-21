##
from flask imp
ort Flask, request, url_for, redirect

app=Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def welcome():
	return "Welcome, This is My first web app!!!"

#Basic
@app.route("/hello")
def hello():
	return "Hello!!!"

#Variable
@app.route("/hello/<name>")
def helloname(name):
	return "Hello %s!!!" % name

@app.route("/hello/<int:roll>")
def Roll_Num(roll):
	return "Roll Number %d!!!" % roll

@app.route("/hello/<float:per>")
def percentage(per):
	if per >= 40:
			return "Congratulations!!! You got %f Percent!!!" % per
	else:
		return "Sorry!!! You got %f Percent!!!" % per

#redirect, url_for
@app.route("/user/<name>")
def user(name):
	if name == "admin":
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest = name))

@app.route("/hello_admin")
def hello_admin():
	return "Hello Admin!!!"

@app.route("/hello_guest/<guest>")
def hello_guest(guest):
	return "Hello %s as Guest!!!" % guest

#Login request
@app.route("/login")
def login_page():
	req_data = request.args
	if req_data['username']=='admin' and req_data['pass']=='pwd':
		return "Success!!!"
	else:
		return "Failure!!!"

if __name__ == "__main__":
	app.run(host="127.0.0.1", debug="true", port = 8090)

##
