from flask import Flask, render_template, request, url_for
app = Flask("Cryptocurrency")
login_dict = {"nishant@gmail.com":"12345"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    r_email = request.args.get("email_r")
    r_password = request.args.get("password_r")
    new_dict = {r_email:r_password}
    login_dict.update(new_dict)
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/prediction")
def prediction():
    return render_template("index.html")

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0', port='80')