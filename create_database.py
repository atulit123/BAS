import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
##creating table book
query_create_book="""
CREATE TABLE if not exists book (
    book_id int not null,
    isbn varchar(255) not null,
    title varchar(255) not null,
    author text not null,
    mrp decimal not null,
    cost_price decimal not null,
    stock int not null,
    genre text not null,
    image_path text not null,
    primary key(book_id)
);
 
"""


# For creating create db
# Below line  is hide your warning 
#cursor.execute("SET sql_notes = 0; ")
# create db here....
#cursor.execute("create database IF NOT EXISTS BAS")
cursor.execute(query_create_book)

#commit changes
db.commit()

print "created database"

## Close the connection
db.close()
