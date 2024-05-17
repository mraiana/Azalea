import sqlite3

# Функция для создания базы данных и таблицы цветов
def create_database():
    conn = sqlite3.connect('flowers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS flowers (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT,
                    price REAL,
                    quantity INTEGER,
                    image_path TEXT
                )''')
    conn.commit()
    conn.close()

# Функция для получения информации о цветах из базы данных
def get_all_flowers():
    conn = sqlite3.connect('flowers.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM flowers''')
    flowers = c.fetchall()
    conn.close()
    return flowers

# Функция для добавления цветка в базу данных
def add_flower(name, description, price, quantity, image_path):
    conn = sqlite3.connect('flowers.db')
    c = conn.cursor()
    c.execute('''INSERT INTO flowers (name, description, price, quantity, image_path)
                 VALUES (?, ?, ?, ?, ?)''', (name, description, price, quantity, image_path))
    conn.commit()
    conn.close()

# Функция для обновления информации о цветке в базе данных
def update_flower(name, description, price, quantity, image_path, flower_id):
    conn = sqlite3.connect('flowers.db')
    c = conn.cursor()
    c.execute('''UPDATE flowers SET name=?, description=?, price=?, quantity=?, image_path=? WHERE id=?''',
              (name, description, price, quantity, image_path, flower_id))
    conn.commit()
    conn.close()

# Функция для удаления цветка из базы данных
def delete_flower(flower_id):
    conn = sqlite3.connect('flowers.db')
    c = conn.cursor()
    c.execute('''DELETE FROM flowers WHERE id=?''', (flower_id,))
    conn.commit()
    conn.close()

# Создаем базу данных, если она еще не существует
create_database()

