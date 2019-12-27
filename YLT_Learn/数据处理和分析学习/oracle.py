import cx_Oracle

conn = cx_Oracle.connect('scott/admin@myoracle')

cursor = conn.cursor()
sql_string = "SELECT * from emp"
a = cursor.execute(sql_string)
print(a)
