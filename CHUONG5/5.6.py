import sqlite3

database_name = "my_database.db"
table_name = "users"

connection = sqlite3.connect(database_name)
cursor = connection.cursor()

cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
count = cursor.fetchone()[0]
print(f"Số bản ghi trong bảng {table_name}: {count}")

connection.close()
