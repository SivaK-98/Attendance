from flask import Flask, render_template, request
import mongo_db

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/signup_page', methods=['POST', 'GET'])
def signup_page():
  return render_template("signup.html")


@app.route("/signup", methods=["POST", "GET"])
def signup():
  if request.method == 'POST':
    name = request.form.get("name")
    roll = request.form.get("roll")
    email = request.form.get("email")
    password = request.form.get("password")
    data = {"name": name, "roll": roll, "email": email, "password": password}
    print(data)
    response = mongo_db.signup(data)
    if response == True:
      return render_template("login.html")
    else:
      return render_template("signup.html", error=response)
  else:
    return render_template("signup.html", error=response)


@app.route("/login", methods=["POST", 'GET'])
def login():
  if request.method == 'POST':
    email = request.form.get("email")
    password = request.form.get("password")
    response = mongo_db.login(email, password)
    data = response
    if data["error"] == None:
      #return render_template("dashboard.html", data=data)
      return "Password matched"
    else:
      return data["error"]
  else:
    return render_template("login.html", error="Login failed")


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)
