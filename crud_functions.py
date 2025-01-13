import sqlite3

data_base = 'products.db'


def initiate_db():
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')

    for i in range(1, 5):
        cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                       (f'Продукт {i}', f'Описание {i}', 100 * i))

    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products


def add_users(username, email, age, balance):
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, balance))
    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect(data_base)
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM Users WHERE username = ?", (username,))
    exist = cursor.fetchone() is not None
    connection.close()
    return exist
