import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
    salary INTEGER,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(id)
);

INSERT INTO departments (id, name) VALUES
(1, 'Разработка'),
(2, 'Маркетинг');

INSERT INTO employees (name, position, salary, department_id) VALUES
('Алексей', 'Разработчик', 120000, 1),
('Мария', 'Тестировщик', 90000, 1),
('Ольга', 'Маркетолог', 80000, 2);
""")

conn.commit()
conn.close()
