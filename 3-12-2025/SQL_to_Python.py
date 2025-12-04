import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="V@ishnav1",
    db="company_db"
)

cursor = conn.cursor()

#-- CRUD Ops
cursor.execute("INSERT INTO employees (emp_id, emp_name, email, salary, dept_id) VALUES (107, 'Manju Rajan', 'manju@example.com', 200000, 40)")
cursor.execute("DELETE FROM employees WHERE emp_id= 104")
cursor.execute("UPDATE employees SET salary=50000 WHERE emp_id= 105")
cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()