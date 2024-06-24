from flask import Flask, render_template, request
from flask.json import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        role = request.form.get("role")
        print(email)
        return email
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
