import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
##creating table book
query_create_customer="""
CREATE TABLE if not exists cart (
    user_name varchar(255) not null,
    book_id int not null,
    amount int not null
);
 
"""


# For creating create db
# Below line  is hide your warning 
#cursor.execute("SET sql_notes = 0; ")
# create db here....
#cursor.execute("create database IF NOT EXISTS BAS")
cursor.execute(query_create_customer)

#commit changes
db.commit()

print "created table"

## Close the connection
db.close()
