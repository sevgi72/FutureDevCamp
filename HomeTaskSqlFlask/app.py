from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_NAME = "heroes_yeni.db" 

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS heroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            health INTEGER,
            power INTEGER,
            class TEXT
        )
        """)
        
        heroes = [
            ("Arthur", 100, 80, "Warrior"),
            ("Merlin", 80, 95, "Mage"),
            ("Robin", 90, 75, "Archer"),
            ("Thor", 120, 100, "Warrior"),
            ("Gandalf", 85, 98, "Mage")
        ]
        
        cursor.executemany("""
        INSERT INTO heroes (name, health, power, class)
        VALUES (?, ?, ?, ?)
        """, heroes)
        
        conn.commit()
        conn.close()
        print("Məlumat bazası və qəhrəmanlar uğurla yaradıldı!")

# Digər kodlar eynilə qalır...
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def welcome():
    return "Welcome to RPG Hero System"

@app.route('/heroes')
def get_all_heroes():
    conn = get_db_connection()
    heroes_rows = conn.execute("SELECT * FROM heroes").fetchall()
    conn.close()
    heroes_list = [dict(row) for row in heroes_rows]
    return jsonify(heroes_list)

@app.route('/hero/<int:id>')
def get_hero_by_id(id):
    conn = get_db_connection()
    hero_row = conn.execute("SELECT * FROM heroes WHERE id = ?", (id,)).fetchone()
    conn.close()
    if hero_row is None:
        return "Qəhrəman tapılmadı!", 404
    return jsonify(dict(hero_row))

@app.route('/mages')
def get_mages():
    conn = get_db_connection()
    mages_rows = conn.execute("SELECT * FROM heroes WHERE class = 'Mage'").fetchall()
    conn.close()
    mages_list = [dict(row) for row in mages_rows]
    return jsonify(mages_list)

@app.route('/strong')
def get_strong_heroes():
    conn = get_db_connection()
    strong_rows = conn.execute("SELECT * FROM heroes WHERE power > 80").fetchall()
    conn.close()
    strong_list = [dict(row) for row in strong_rows]
    return jsonify(strong_list)

@app.route('/battle/<int:id1>/<int:id2>')
def battle(id1, id2):
    conn = get_db_connection()
    hero1 = conn.execute("SELECT * FROM heroes WHERE id = ?", (id1,)).fetchone()
    hero2 = conn.execute("SELECT * FROM heroes WHERE id = ?", (id2,)).fetchone()
    conn.close()
    
    if not hero1 or not hero2:
        return "Döyüşçülərdən biri və ya hər ikisi tapılmadı!", 404
    
    if hero1['power'] > hero2['power']:
        return f"{hero1['name']} wins!"
    elif hero2['power'] > hero1['power']:
        return f"{hero2['name']} wins!"
    else:
        return "It's a tie!"

if __name__ == '__main__':
    init_db()  
    app.run(debug=True)