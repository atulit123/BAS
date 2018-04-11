import MySQLdb

# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
user_name="atulit123"
##creating table book
search_query="""
SELECT * FROM cart INNER JOIN book on cart.book_id=book.book_id
WHERE cart.user_name=%s
"""


# For creating create db
# Below line  is hide your warning 
#cursor.execute("SET sql_notes = 0; ")
# create db here....
#cursor.execute("create database IF NOT EXISTS BAS")
cursor.execute(search_query,(user_name))
results=list(cursor.fetchall())
print results[0]
#commit changes
db.commit()

print "created table"

## Close the connection
db.close()
