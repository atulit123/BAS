import MySQLdb
import numpy as np
import pickle
# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="atulit",db="bas")

cursor = db.cursor()
##creating table book
insert_book="""
INSERT INTO book (isbn,author,title,book_id,image_path,mrp,cost_price,genre,stock)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""
genre_list=["Thriller","Suspense","Tragedy","Drama","Sci-fi","fiction","tell-all","cross-genre","general"]

# For creating create db
# Below line  is hide your warning 
#cursor.execute("SET sql_notes = 0; ")
# create db here....
#cursor.execute("create database IF NOT EXISTS BAS")

data=pickle.load(open("dataset.pkl","rb"))
print(data)
for d in data:
    mrp=np.random.randint(100,5000)
    cost_price=np.random.randint(100,mrp)
    genre=genre_list[np.random.randint(len(genre_list))]
    stock=np.random.randint(500)
    cursor.execute(insert_book,(d[0],d[1],d[3],d[4],d[5],mrp,cost_price,genre,stock))

#commit changes
db.commit()

print "created database"

## Close the connection
db.close()
