from flask import Flask, render_template, request, url_for, redirect

from werkzeug.security import generate_password_hash, check_password_hash
import time
import random
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Rauf_Russian_People'

connect = sql.connect('users.db', check_same_thread=False)
cursor = connect.cursor()


@app.get("/")
def home():
    return render_template("home.html")


@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    message  = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email, password)
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            message = 'User is already registered'
            return render_template('signup.html', message=message)
        else:
                hash = generate_password_hash(password)
                data = (str(email), str(hash[7:]))
                cursor.execute("INSERT INTO users (email, hash) VALUES (?,?)", data)
                connect.commit()
                return redirect(url_for("home"))
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
