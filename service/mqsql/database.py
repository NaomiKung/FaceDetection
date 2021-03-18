import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user = "test",
    password = 'Test_123',
    database = 'learn_sql'
)

mycursor = mydb.cursor()
if 1 < 2:
    sql = "INSERT INTO albums (artist, album, released, genre, sales_in_millions) VALUES (%s,%s,%s,%s,%s)"
    val = ("Krit","เพลง","2020","rock","1")
    mycursor.execute(sql, val)
    mydb.commit()


mycursor.execute("SELECT * FROM albums")
my_result = mycursor.fetchall()

print(my_result[-1])