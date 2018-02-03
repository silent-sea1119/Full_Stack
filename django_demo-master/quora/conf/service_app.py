import django
django.setup()

from flask import Flask, request, jsonify
from quora.db.quora.models import User

app = Flask(__name__)

@app.route("/")
def welcome():
    return "WELCOME..."
@app.route("/user")
def create_user():

    request_data = request.args
    print request_data
    try:
        user_object = User.objects.create(username=request_data['username'], password=request_data['password'],
                                          mobile_number=int(request_data['mobileNumber']))
    except Exception as e:
        print e
    response_dict = {"username": user_object.username,
                     "password": user_object.password,
                     "mobileNumber": user_object.mobile_number}
    return jsonify(response_dict)

@app.route("/getUser")
def get_user():
    res = []
    for x in User.objects.all():
        res1 = x.username
        res.append(res1)
    return jsonify(res)

@app.route("/getUser/<name>")
def get_userx(name):
    for x in User.objects.all():
        if x.username == name:
            return  x.username+" Found...!!"
    return "Not Found...!!"

@app.route("/getUserStart/<start>")
def get_userS(start):
    lst = list(User.objects.filter(username__startswith = start).values("username"))
    return jsonify(lst)

@app.route("/deleteUser/<name>")
def del_user(name):
    for x in User.objects.all():
        if x.username == name:
            User.objects.filter(username = x.username).delete()
            return x.username + " Deleted Successfully...!!"
    return "Username Not Found...!!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2004, debug=True)
