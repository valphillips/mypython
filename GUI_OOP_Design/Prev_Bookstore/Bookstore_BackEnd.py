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
        self.conn=sqlite3.connect(db)  #If passing in DB name as parameter
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    #   id field will automatically assign values  due to the type defined
        self.conn.commit()
 

    def view(self):
        print("*** Executing view")
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, title="",author="",year="",isbn=""):
        print("*** Executing search")
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows


    def insert(self,title,author,year,isbn):
        print("*** Executing insert")
        self.cur.execute("INSERT INTO book (title,author,year,isbn) VALUES(?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        print("*** Executing update")
        self.cur.execute("UPDATE book set title=?,author=?,year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def delete(self,id):
        print("*** Executing delete")
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):   #This is executed when we exit the class
        print("Closing database")
        self.conn.close()


#print("Before calling connect function")
#connect()
#print("After calling connect function")
#print(view())

#insert("Test Title 2","My Author 2",1976,1454587438787)
#insert("The Earch","John Smith",1918,913134343543)
#insert("The Sun","John Candy",1978,91883784343543)
#print(search(author="The Sun"))
#delete(1)
#update(3,"The moon","John Candy",1978,91883784343543)
