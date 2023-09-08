import sqlite3

# creating connection to a new database
db = sqlite3.connect("books-collection.db")

# cursor which controls database
cursor = db.cursor()

# .execute tells the cursor to execute a command which are usually in all caps
# The part inside parenthesis after create table are the columns or the fields of the table
# The primary key is the one piece of data that will uniquely identify this record in the table.
#  rating FLOAT NOT NULL -  A field that accepts FLOAT data type numbers, cannot be empty and the field is called rating.
cursor.execute("CREATE TABLE books "
               "(id INTEGER PRIMARY KEY, "
               "title varchar(250) NOT NULL UNIQUE, "
               "author varchar(250) NOT NULL, "
               "rating FLOAT NOT NULL)")

# adds data into our table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()