from flask import Flask, render_template, request,session
from flask.json import jsonify
import mongodb

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        password = request.form.get("password")
        register = request.form.get("register")
        role = request.form.get("role")
        response = mongodb.signup(name,email, phone, register, role, password)
        print(response)
        user = session.get(name)
        return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
