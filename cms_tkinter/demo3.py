import pymysql

con=pymysql.connect('localhost', 'root', '', 'CustomerDb')
cursor=con.cursor()

qry="select * from customer;"
cursor.execute(qry)
val=cursor.fetchall()

f=open("E://customerlist.xls", "w+")

for tup in val:
    for el in tup:
        f.write(str(el)+'\t')
    f.write('\n')

f.close()

con.close()