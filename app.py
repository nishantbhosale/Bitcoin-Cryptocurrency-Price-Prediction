"""from crypt import methods
import email
from urllib import request"""
from flask import Flask, render_template, request, url_for

app = Flask("Cryptocurrency")
login_dict = {"nishant@gmail.com":"12345"}
@app.route("/")
def home():
	r_email = request.args.get("email_r")
	r_password = request.args.get("password_r")
	new_dict = {r_email:r_password}
	login_dict.update(new_dict)
	return render_template("index.html")
    
@app.route("/register", methods=["GET"])
def register_a():
	return render_template("register.html")

@app.route("/prediction", methods=["GET"])
def prediction_m():
	emaill = request.args.get("email")
	passwordd = request.args.get("password")
	if emaill in login_dict:
		if passwordd == login_dict.get(emaill):
			return render_template("prediction.html")

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port='80', debug=True)




