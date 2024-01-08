import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables = cursor.fetchall()

print("Các bảng trong cơ sở dữ liệu:")
for table in tables:
      print(table[0])

connection.close()