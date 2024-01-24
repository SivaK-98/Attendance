from flask import Flask, render_template, request
import mongo_db

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("login.html")


@app.route("/signup", methods=['POST', 'GET'])
def signup():
  if request.method == "POST":
    print("Executing Signup command")
    email = request.form.get("email")
    roll_number = request.form.get("roll_number")
    mobile = request.form.get("number")
    password = request.form.get("password")
    role = request.form.get("role")
    print(
        f"Email: {email} \nRoll Number: {roll_number} \nMobile: {mobile}\nPassword: {password}\nrole: {role}"
    )
    result = mongo_db.signup(email, roll_number, mobile, password, role)
    if result == True:
      return render_template("login.html")
    elif result == "duplicate":
      return "ID already used"

@app.route('/signup_page',methods=['POST', 'GET'])
def signup_page():
  return render_template("signup.html")

@app.route("/login", methods=['POST', 'GET'])
def login():
  if request.method == "POST":
    email = request.form.get("email")
    password = request.form.get("password")
    result = mongo_db.login(email, password)
    role = result["role"]
    account_id = result["account_id"]
    print("Role:",role)
    print("Account ID:",account_id)
    if role == "admin":
      return render_template("admin.html", account_id=account_id)
    elif role == "staff":
      return render_template("staff.html", account_id=account_id)
    elif role == "student":
      return render_template("student.html", account_id=account_id, roll_number=roll_number)
    else:
      return "Invalid Role"
                                                        
@app.route("/add_staff", methods=["POST", "GET"])
def add_staff():
  if request.method == "POST":
    name = request.form.get("name")
    email = request.form.get("email")
    roll_number = request.form.get("roll_number")
    mobile = request.form.get("number")
    role = request.form.get("role")
    print("NAME:", name)
    if role == "staff":
      result = mongo_db.add_staff(name, email,roll_number,mobile,role)
      if result == True:
        return "Staff added successfully"
    elif role == "student":
      result = mongo_db.add_student(name, email,roll_number,mobile,role)
      if result == True:
        return "Student added successfully"
    else:
      return "Invalid Role"

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)
