import csv 
import sqlite3

conn =sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""create table if not exist users(id integer primary key autoincrement,
                    name varchar(20)  notnull
                    email varchar(20) notnull)
""")

with open("users.csv","r") as file:
     reader = csv.DcitReader(file)
     for  row in reader:
          name= row.get("name")
          email= row.get("email")

          if name and email:
             cursor.execute(insert into users(name,email)values(?,?)",(name,email))

conn.commit()
conn.close()



