from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('school.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Welcome to Student Management"

@app.route('/students')
def get_all_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    
    output = []
    for student in students:
        output.append({'id': student['id'], 'name': student['name'], 'age': student['age']})
    return jsonify(output)


@app.route('/student/<int:id>')
def get_student(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if student is None:
        return "Student Not Found", 404
        
    return jsonify({'id': student['id'], 'name': student['name'], 'age': student['age']})

@app.route('/candrivecars')
def can_drive_cars():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students WHERE age >= 18').fetchall()
    conn.close()
    
    output = []
    for student in students:
        output.append({'id': student['id'], 'name': student['name'], 'age': student['age']})
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)