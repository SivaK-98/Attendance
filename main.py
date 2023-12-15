from flask import Flask, render_template, request
import mongo_db

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("home.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
  if request.method == "POST":
    print("Executing login command")
    email = request.form.get("email")
    roll_number = request.form.get("roll_number")
    mobile = request.form.get("number")
    password = request.form.get("password")
    role = request.form.get("role")
    print(
        f"Email: {email} \nRoll Number: {roll_number} \nMobile: {mobile}\nPassword: {password}\nrole: {role}"
    )
    result = mongo_db.signup(email, roll_number, mobile, password, role)
    print(result)
    return render_template("home.html")


if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)
