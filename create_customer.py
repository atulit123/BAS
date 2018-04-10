import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
##creating table book
query_create_customer="""
CREATE TABLE if not exists customer (
    user_name varchar(255) not null,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255) not null,
    password varchar(255) not null,
    address varchar(255) not null,
    primary key(user_name)
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
