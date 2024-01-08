import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute("SELECT SQLITE_VERSION()")
version = cursor.fetchone()
print(f"Phiên bản của SQLite: {version[0]}")
connection.close()