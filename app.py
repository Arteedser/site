from flask import Flask, render_template, request, url_for, redirect

import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

with open('psswdroot.txt', 'r') as f:
    root_psswd = f.read()

app = Flask(__name__)
sql = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f"{root_psswd}",
    database='users'
)
app.config['SECRET_KEY'] = 'Rauf_Russian_People'

cursor = sql.cursor()


@app.get("/")
def home():
    return render_template("home.html")


@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        surname = request.form["surname"]
        password2 = request.form["password2"]
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            message = 'User is already registered'
            return render_template('signup.html', message=message)
        elif 6 > len(password) > 16 or password.isdigit() or password.isalpha():
            message = 'The password must be 8 to 16 characters long and contain letters and numbers'
            return render_template('signup.html', message=message)
        elif password != password2:
            message = "Passwords don't match"
            return render_template('signup.html', message=message)
        else:
            hash = generate_password_hash(password)
            data = (str(email), str(hash), surname)
            cursor.execute("INSERT INTO users (email, hash_psswd, surname) VALUES (%s, %s, %s)", data)
            sql.commit()
            return redirect(url_for("home"))
    return render_template("signup.html")


if __name__ == '__main__':
    app.run(debug=True)
