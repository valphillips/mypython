"""
Backend for the bookstore app

"""
import sqlite3



# Execute the function to connect to DB
#connect()

class Database:
    
    def __init__(self, db):  # This defines this function as the 'constructor' that is called when the class is called
#   def __init__(self):  # e.g. if the database name is defined inside this back-end, rather than being passed in as parameter

        print("*** Executing connect")
        conn=sqlite3.connect(db)  #If passing in DB name as parameter
    #   conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    #   id field will automatically assign values  due to the type defined
        conn.commit()
        conn.close()



    def view(self):
        print("*** Executing view")
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()
        return rows


    def search(self, title="",author="",year="",isbn=""):
        print("*** Executing search")
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?",(title,author,year,isbn))
        rows=cur.fetchall()
        conn.close()
        return rows


    def insert(self,title,author,year,isbn):
        print("*** Executing insert")
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book (title,author,year,isbn) VALUES(?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()

    def update(self,id,title,author,year,isbn):
        print("*** Executing update")
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book set title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        conn.commit()
        conn.close()

    def delete(self,id):
        print("*** Executing delete")
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()


print("Before calling connect function")
#connect()
#print("After calling connect function")
#print(view())

#insert("Test Title 2","My Author 2",1976,1454587438787)
#insert("The Earch","John Smith",1918,913134343543)
#insert("The Sun","John Candy",1978,91883784343543)
#print(search(author="The Sun"))
#delete(1)
#update(3,"The moon","John Candy",1978,91883784343543)
