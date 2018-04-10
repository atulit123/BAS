import MySQLdb
import numpy as np
import pickle
# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
##creating table book
insert_customer="""
INSERT INTO customer (user_name,first_name,last_name,email,phone,password,address
)
VALUES (%s,%s,%s,%s,%s,%s,%s)
"""


# For creating create db
# Below line  is hide your warning 
#cursor.execute("SET sql_notes = 0; ")
# create db here....
#cursor.execute("create database IF NOT EXISTS BAS")


cursor.execute(insert_customer,("atulit123","Atulit","Kumar","ak8087960@gmail.com","7077105401","1234","F-229,Hall 80")
          )

db.commit()
print "created database"

## Close the connection
db.close()
