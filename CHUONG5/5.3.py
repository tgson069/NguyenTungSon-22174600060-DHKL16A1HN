import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  'Tên' TEXT,
                  'Tuổi' INTEGER
                  )''')

connection.commit()
connection.close