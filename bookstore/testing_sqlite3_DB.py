import sqlite3

def create_table():
    # This will either create the database if it doesn't exist, or connect to your existing DB)
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
#   cur.execute("INSERT INTO store VALUES ('Wine Glass',8, 10.5) ") 
    cur.execute("INSERT INTO store VALUES (?,?,?)", (item,quantity,price)) 
    conn.commit()
    conn.close()

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    # Note the syntax below were we specify the parameter - need to add , after
    # (item,)
    cur.execute("DELETE FROM store where ITEM=?", (item,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? where ITEM=?", (quantity,price,item))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows   

create_table()
#insert("Water Glass", 10, 5)
#insert("Coffee Cup", 10, 5)


#Read the table and display the rows
rows=view()
for row in rows:
    print(row)
    
# delete("Coffee Cup")
update("Water Glass", 9,5.6)

#Read the table and display the rows
rows=view()
for row in rows:
    print(row)
