from flask import Flask, render_template, request, url_for, redirect
'''
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
'''
app = Flask(__name__)
'''sql = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="121377Rr.",
    database='users'
)'''
app.config['SECRET_KEY'] = 'Rauf_Russian_People'

# cursor = sql.cursor()


@app.get("/")
def home():
    return render_template("home.html")

'''
@app.route("/SignUp", methods=["GET", "POST"])
def SignUp():
    message = ""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email, password)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        existing_user = cursor.fetchone()
        if existing_user:
            message = 'User is already registered'
            return render_template('signup.html', message=message)
        else:
            hash = generate_password_hash(password)
            data = (str(email), str(hash))
            cursor.execute("INSERT INTO users (email, hash_psswd) VALUES (%s, %s)", data)
            sql.commit()
            return redirect(url_for("home"))
    return render_template("signup.html")
'''

if __name__ == '__main__':
    app.run(debug=True)
