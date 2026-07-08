from flask import Flask, render_template

app = Flask(__name__)

# Tələbə məlumatları (Database əvəzi)
students = {
    1: "Murad",
    2: "Leyla",
    3: "Aysel",
    4: "Aysu",
    5: "Elcan"
}

# Welcome Page
@app.route("/")
def home():
    return render_template("home.html")

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

# Show all students
@app.route("/students")
def all_students():
    # students lüğətini HTML faylına göndəririk
    return render_template("students.html", students=students)

# Show student by ID
@app.route("/student/<int:id>")
def student(id):
    if id in students:
        return f"<h3>Student ID: {id}</h3><p>Student Name: {students[id]}</p><br><a href='/students'>Siyahıya qayıt</a>"
    else:
        return "<h3>Student not found!</h3><br><a href='/students'>Siyahıya qayıt</a>", 404


@app.route("/profile/<username>")
def profile(username):
    return f"Hello, {username}! Welcome to your profile."

if __name__ == "__main__":
    app.run(debug=True)