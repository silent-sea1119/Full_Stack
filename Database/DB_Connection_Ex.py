import MySQLdb

db = MySQLdb.connect("localhost", "root", "akshay123", "mydb")

cursor = db.cursor()

cursor.execute("insert into login values('akshay1', 'akshay1234');")

db.commit()

db.close()
