import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="agenda"
)
cursor = connection.cursor()

data = ("Maria","maria.azevedo@gmail.com","551235879017","do you breathe?")

cursor.execute("insert into users (namee, email, phone, message) values(%s,%s,%s,%s)", data)

connection.commit()

cursor.execute("select * from users")

result = cursor.fetchall()

print(result)

connection.close()