from flask import Flask, render_template

app = Flask(__name__)

# 1. Ana Səhifə (/)
@app.route('/')
def home():
    return render_template('home.html')

# 2. Haqqımda səhifəsi (/about)
@app.route('/about')
def about():
    return render_template('about.html')

# 3. Bacarıqlar səhifəsi (/skills)
@app.route('/skills')
def skills():
    # Ən azı 5 bacarıqdan ibarət Python list-i
    skills_list = ["Python", "Flask", "SQL", "Git", "HTML/CSS"]
    return render_template('skills.html', skills=skills_list)

# 4. Dinamik profil səhifəsi (/profile/<username>)
@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username)

# 5. Tələbə axtarışı (/student/<int:id>)
@app.route('/student/<int:id>')
def student(id):
    # Tələbə məlumatlarını saxlayan dictionary
    students_db = {
        1: "Əli",
        2: "Vəli",
        3: "Aysel",
        4: "Leyla"
    }
    student_name = students_db.get(id) # ID yoxdursa None qaytarır
    return render_template('student.html', name=student_name, student_id=id)

# ⭐ Bonus: İki ədədin cəmi (/sum/<int:a>/<int:b>)
@app.route('/sum/<int:a>/<int:b>')
def sum_numbers(a, b):
    total = a + b
    return render_template('sum.html', num1=a, num2=b, result=total)

if __name__ == '__main__':
    app.run(debug=True)