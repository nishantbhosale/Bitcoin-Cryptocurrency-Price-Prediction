from flask import Flask, render_template,request,flash,redirect,url_for,session
import sqlite3, http.client
from flask_sqlalchemy import SQLAlchemy


app = Flask("Cryptocurrency")
app.secret_key="123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
print(db)
con=sqlite3.connect("data.db")
con.execute("create table if not exists person(id integer primary key,name text,email text NOT NULL UNIQUE,password text)")
con.close()
print(con)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=='POST':
        #name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        con=sqlite3.connect("data.db")
        con.row_factory=sqlite3.Row
        cur=con.cursor()
        cur.execute("select * from person where email=? and password=?",(email,password))
        data=cur.fetchone()

        if data:
            session["email"]=data["email"]
            session["password"]=data["password"]
            return redirect("/prediction")
            #return render_template("prediction.html")
        else:
            return redirect("/MisMatch")
            #return("Username and Password Mismatch")
            #flash("Username and Password Mismatch","danger")
    #return redirect(url_for("login"))
    return render_template("login.html")

@app.route("/MisMatch")
def MisMatch():
    return render_template("MisMatch.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=='POST':
        try:
            name=request.form['name']
            email=request.form['email']
            password=request.form['password']
            #db=sqlite3.connect("data.db")
            #db.session.add(name, email, password)
            #mail=request.form['mail']
            con=sqlite3.connect("data.db")
            cur=con.cursor()
            cur.execute("insert into person(name,email,password)values(?,?,?);",(name,email,password))
            con.commit()
            print("Record Added  Successfully")
            flash("Record Added  Successfully","success")
        except:
            print("Error in Insert Operation","danger")
            flash("Error in Insert Operation","danger")
        finally:
            return redirect(url_for("login"))
            con.close()

    return render_template("registration.html")

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    if request.method=='POST' or request.method=='GET':
        #return("It's working bro")
        return render_template("prediction.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == '__main__' :
    db.create_all()
    app.run(debug=True, host='0.0.0.0', port='80')