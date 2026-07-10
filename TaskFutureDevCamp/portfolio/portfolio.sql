-- profile cədvəlinin yaradılması
CREATE TABLE IF NOT EXISTS profile (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    profession TEXT NOT NULL,
    about TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL
);

INSERT INTO profile (name, profession, about) 
VALUES ('Sevgi Farajli', 'Backend Developer | Information Security Student at UNEC', 'I have a huge passion for technology, coding, and cyber security');

INSERT INTO projects (title, description) 
VALUES 
('Pustok', 'ASP.NET Core MVC Web Application.'),
('Juan', 'ASP.NET Core MVC Web Application.'),
('BankAPI', 'RESTful Web API for Banking Systems.'),
('Piquant', 'Front-end Web Application built with HTML/CSS/JS.');