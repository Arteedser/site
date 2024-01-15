from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
