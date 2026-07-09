import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')

cursor.execute("SELECT COUNT(*) FROM students")
if cursor.fetchone()[0] == 0:
    students_data = [
        ('huseyn memmedov', 20),
        ('gunel musazade', 17),
        ('Kənan Əliyev', 19),
        ('Lalə Həsənova', 16),
        ('Rəşad Hüseynov', 22)
    ]
    cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students_data)
    conn.commit()
    print("database ve telebeler yaradildi ve melumatlar daxil edildi")
else:
    print("database artiq movcuddur")

conn.close()