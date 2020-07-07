import cx_Oracle

conn1 = cx_Oracle.connect('mbsdb/mbsdb@localhost/orcl')
# conn2 = cx_Oracle.connect('mbsdb/mbsdb@172.0.17.226/mbsdb')
curs1 = conn1.cursor()
# curs2 = conn2.cursor()
sql1 = "SELECT SUBSTR(献血码,1,3) || '******' || SUBSTR(献血码,10,4) AS 献血码 FROM DONOR_TEST WHERE 证件类别='身份证'"
# sql2 = 'SELECT TABLE_NAME,TABLESPACE_NAME,NUM_ROWS FROM user_tables ORDER BY NUM_ROWS desc'
curs1.execute(sql1)
data = curs1.fetchall()
for i in data:
    print(i)
curs1.close()
# curs2.close()
conn1.close()
# conn2.close()
