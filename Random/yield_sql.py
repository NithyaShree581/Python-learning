import mysql.connector
connection=mysql.connector.connect(host="localhost",user="root",password="Nithyamradhe@12",database="employees")
cursor=connection.cursor()
def employeefetcher(cursor):
        cursor.execute("select * from employees limit 5000" )
        while True:
            rows=cursor.fetchmany(10)
            if not rows:
                break
            yield rows
i=1
for employee in employeefetcher(cursor):
    print("total no of rows is",10*i)
    print(employee) 
    i+=1
cursor.close()
connection.close()