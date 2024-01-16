import sqlite3 as sql

connect = sql.connect('users.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute("""CREATE TABLE users 
(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
email TEXT NOT NULL ,
hash TEXT NOT NULL 
)
""")


connect.commit()