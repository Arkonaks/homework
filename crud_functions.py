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
