import index
import mysql.connector ,os
data = os.environ 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Akash@123",
  database="Assigment"
)

mycursor = mydb.cursor()

def create_table():
    mycursor.execute("SELECT COUNT(*)FROM information_schema.tables WHERE table_name = 'movie_detail'")
    if mycursor.fetchone()[0] == 1:
        mycursor.close()
        print("Table already created..")
    else:
        try:
            mycursor.execute("CREATE TABLE movie_detail (movie_name VARCHAR(255), release_date VARCHAR(255))")
            print("Table created successfuly..")
        except:
            print("Table does not create..Something went wrong..")
create_table()


def insert_data():
    mycursor = mydb.cursor()
    for i in data:
        sql = "INSERT INTO movie_detail (movie_name, release_date) VALUES (%s, %s)"
        val = (i["movie_name"], i["release_date"])
        mycursor.execute(sql, val)
        mydb.commit()
    print("data inserted successfuly")
insert_data()


def read_data():
    quary = mydb.cursor()
    quary.execute('select * from movie_detail')
    mo_data= quary.fetchall()
    if len(mo_data):
        print(mo_data)
    else:
        print("Table is Empty..")
read_data()



