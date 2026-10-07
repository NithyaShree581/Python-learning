import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    connection_timeout=10,
    use_pure=True
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM employees LIMIT 10")

rows = cursor.fetchall()

print(cursor.column_names)

for row in rows:
    print(row)

cursor.close()
connection.close()