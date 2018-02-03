from flask import Flask,request
import MySQLdb
import json

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", "akshay123", "mydb")
cursor = db.cursor()

@app.route("/")
def welcome():
	return "Welcome, Database Connection Program!!!"

@app.route("/login")
def logindb():
	req_data = request.args
	uname = req_data['username']
	pwd = req_data['pass']
	cursor.execute("select * from login where username = %s AND password = %s", [uname, pwd] )
	result = cursor.fetchall()
	if result:
		return "Success...!!!"
	else:
		return "Failed...!!!"

@app.route('/user')
def print_users():
	cursor.execute("select * from login")
	entries = cursor.fetchall()
	res_data = []
	for entry in entries:
		res_dict = {}
		res_dict['username'] = entry[0]
		res_dict['password'] = entry[1]
		res_data.append(res_dict)
	response_dict = {"data" : res_data}
	return json.dumps(response_dict)
		
if __name__ == "__main__":
	app.run(host="127.0.0.1", port =8092, debug="true")
