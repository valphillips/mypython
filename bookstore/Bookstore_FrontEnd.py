"""
A program that stores this book information:
Title, Author, Year, ISBN

User can:

View all records
Search an entry
Add entry
Update entry
Delete
Close

Need Labels, Entry fields, Listbox, Scrollbar, Buttons
Make a drawing of what you want the screen to look like and work from that


Bind method - binds a function to a widget (eg. listbox)
"""

from tkinter import *
from Bookstore_BackEnd import Database  # Use this code if we are calling the 'Database' class in the backend script

database=Database("books.db")  #Create a database object/instance

# Use the syntax below if we are just calling functions in the backend script Iinstead of using the Database class
# import Bookstore_BackEnd
# Bookstore_BackEnd.connect()


#This is the function that is bound to the Listbox event
def get_selected_row(event):
    try:
        global selected_tuple                   #Define global variable accessible outside function
        if list1.size() > 0:
            index=list1.curselection()[0]           #The index is returned in a tuple.  Get the first item in the selection (item 0)
            selected_tuple=list1.get(index)         #Fetch the row with index of the current row
            e1.delete(0, END)                       #Clear the text entry fields and populate them with the selected row
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e1.insert(END,selected_tuple[1])
            e2.insert(END,selected_tuple[2])
            e3.insert(END,selected_tuple[3])
            e4.insert(END,selected_tuple[4])
    except IndexError:
        pass
    
#   Get the value from the e1_value string StringVar function
def set_values():
    print('Set Value')
#    kg=float(e2_value.get())
#    grams=kg*1000
#    pounds=kg*2.20462
#    ounces=kg*35.274
#   Clear up any previous values
#    t1.delete("1.0", END)
#    t2.delete("1.0", END)
#    t3.delete("1.0", END)
#   Now insert the value retrieved into the display fields - at the End)
#    t1.insert(END,round(grams,1))
#    t2.insert(END,round(pounds,4))
#    t3.insert(END,round(ounces,2))


    
def view_command():
    print('View Records')
    list1.delete(0,END)                     #Clear the listbox to start with so that we don't keep appending to it
    for row in database.view():    #Iterate through the tuples passed back for each row in backend code
            list1.insert(END,row)           #Add each new row at the end of the existing rows in the listbox
            
def search_command():
    print('Search Records')
    list1.delete(0,END)
    for row in database.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
            list1.insert(END,row)
    
def add_command():
    print('Add Records')
    database.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)


def delete_command():
    print('Delete Records')
    if list1.size() > 0:
        database.delete(selected_tuple[0])   # Use the global variable that was created by the listbox bound function when record was selected
        view_command()
    
def update_command():
    if list1.size() > 0:
        print('Update Records')
        database.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        print(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
        view_command()


window=Tk()

window.wm_title("BookStore")


        
#Labels
#Title Fields
l1=Label(window,text="Title",height=1,width=10)
l1.grid(row=0, column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text,width=20)
e1.grid(row=0, column=1)

#Author Fields
l2=Label(window,text="Author",height=1,width=10)
l2.grid(row=0, column=2)
author_text=StringVar()
e2=Entry(window,textvariable=author_text,width=20)
e2.grid(row=0, column=3)

#Year Fields
l3=Label(window,text="Year",height=1,width=10)
l3.grid(row=1, column=0)
year_text=StringVar()
e3=Entry(window,textvariable=year_text,width=20)
e3.grid(row=1, column=1)

#ISBN Fields
l4=Label(window,text="ISBN",height=1,width=10)
l4.grid(row=1, column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text,width=20)
e4.grid(row=1, column=3)

#Listbox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Scrollbar
sb1=Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

#Attach scrollbar to list - y=vertical view
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Bind the listbox to function
list1.bind('<<ListboxSelect>>',get_selected_row)


# Buttons 
b1=Button(window,text="View All", height=1,width=12, command=view_command)
b1.grid(row=2, column=3)
b2=Button(window,text="Search Entry", height=1,width=12, command=search_command)
b2.grid(row=3, column=3)
b3=Button(window,text="Add Entry", height=1,width=12, command=add_command)
b3.grid(row=4, column=3)
b4=Button(window,text="Update Selected", height=1,width=12, command=update_command)
b4.grid(row=5, column=3)
b5=Button(window,text="Delete Selected", height=1,width=12, command=delete_command)
b5.grid(row=6, column=3)
b6=Button(window,text="Close", height=1,width=12, command=window.destroy)
b6.grid(row=7, column=3)



# This should always be at the end of your code.
window.mainloop()

