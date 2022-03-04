from flask import Flask, render_template, request, url_for
app = Flask("Cryptocurrency")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("registration.html")

@app.route("/prediction")
def prediction():
    return render_template("index.html")

if __name__ == '__main__' :
    app.run(debug=True, host='0.0.0.0', port='80')