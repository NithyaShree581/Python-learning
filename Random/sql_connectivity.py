import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nithyamradhe@12",
    database="employees"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM employees LIMIT 10")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
connection.close()