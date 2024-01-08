import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INTEGER PRIMARY KEY,
                  'Tên' TEXT,
                  'Tuổi' INTEGER
                  )''')

cursor.execute('''INSERT INTO users ('Tên','Tuổi' )
               VALUES ('Nguyễn Văn A','20')
                  ''')
connection.commit()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for i in rows:
      print(i)
      
connection.close