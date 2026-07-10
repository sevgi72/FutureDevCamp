from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "portfolio_v2.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Yeni bazanı və daxilindəki cədvəlləri sıfırdan quran funksiya"""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            profession TEXT NOT NULL,
            about TEXT NOT NULL
        );
    """)

    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL
        );
    """)

   
    profile_exists = cursor.execute("SELECT COUNT(*) FROM profile").fetchone()[0]
    
    if profile_exists == 0:
        
        cursor.execute("""
            INSERT INTO profile (name, profession, about) 
            VALUES ('Sevgi Farajli', 'Backend Developer | Information Security Student at UNEC', 'I have a huge passion for technology, coding, and cyber security');
        """)

        cursor.executemany("""
            INSERT INTO projects (title, description) VALUES (?, ?);
        """, [
            ('Pustok', 'ASP.NET Core MVC Web Application.'),
            ('Juan', 'ASP.NET Core MVC Web Application.'),
            ('BankAPI', 'RESTful Web API for Banking Systems.'),
            ('Piquant', 'Front-end Web Application built with HTML/CSS/JS.')
        ])

    conn.commit()
    conn.close()

@app.route("/")
def home():
    conn = get_db_connection()
    profile = conn.execute("SELECT * FROM profile LIMIT 1").fetchone()
    projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return render_template("index.html", profile=profile, projects=projects)

@app.route("/about")
def about():
    conn = get_db_connection()
    profile = conn.execute("SELECT * FROM profile LIMIT 1").fetchone()
    conn.close()
    return render_template("about.html", profile=profile)

@app.route("/projects")
def projects():
    conn = get_db_connection()
    projects = conn.execute("SELECT * FROM projects").fetchall()
    conn.close()
    return render_template("projects.html", projects=projects)

if __name__ == "__main__":
    init_db() 
    app.run(debug=True)