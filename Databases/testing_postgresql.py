# Install PostgreSQL from www.postgresql.org/download
# This will also install the PGAdmin tool which is graphical interface to look at the databases
#
# pip install psycopg2 
# (May have issues due to it needing C libraries.  In that case, can either install those, or
# alternatively can install a precompiled version of the package
# www.lfd.uci.edu/~gohlke/pythonlibs/   Psycopg.
# Install the appropriate whl file for your machine e.g.
# Download file: psycopg2-2.6.1-cp35-none-win32.whl and copy to your machine
# Then do > pip install .\psycopg2-2.6.1-cp35-none-win32.whl
#

import psycopg2

# Prerequisite - the postgres database must exist
# Create via pgadmin tool
#
def create_table():
    conn=psycopg2.connect(" dbname='database1' user='postgres' password='admin' host='localhost' port='5432' ") 
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect(" dbname='database1' user='postgres' password='admin' host='localhost' port='5432' ") 
    cur=conn.cursor()
#   cur.execute("INSERT INTO store VALUES ('Wine Glass',8, 10.5) ") 
#   Can insert values using string formatting placeholders as below, but this is prone to SQL injection, so not advised
#   DON't USE !!! cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item,quantity,price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item,quantity,price)) 
    conn.commit()
    conn.close()

def delete(item):
    conn=psycopg2.connect(" dbname='database1' user='postgres' password='admin' host='localhost' port='5432' ") 
    cur=conn.cursor()
    # Note the syntax below were we specify the parameter - need to add , after
    # (item,)
    cur.execute("DELETE FROM store where ITEM=%s", (item,))
    conn.commit()
    conn.close()

def update(item,quantity,price):
    conn=psycopg2.connect(" dbname='database1' user='postgres' password='admin' host='localhost' port='5432' ") 
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s where ITEM=%s", (quantity,price,item))
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect(" dbname='database1' user='postgres' password='admin' host='localhost' port='5432' ") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows   

create_table()

print('\n\nDisplay before executing action ***')
#Read the table and display the rows
rows=view()
for row in rows:
    print(row)
    

#insert("Water Glass", 10, 5)
#insert("Coffee Cup", 10, 5)
#insert("Apple", 6, 2)

#delete("Apple")

update("Water Glass", 9,5.6)

print('\n\nDisplay after executing action ***')
#Read the table and display the rows
rows=view()
for row in rows:
    print(row)
