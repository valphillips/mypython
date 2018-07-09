from tkinter import *


window=Tk()

def km_to_miles():
#   Get the value from the e1_value string StringVar function
    miles=float(e1_value.get())*1.6
#   Now insert the value retrieved into the t1 display field - at the End)
    t1.insert(END,miles)

    
# Button
b1=Button(window,text="Execute", command=km_to_miles)
b1.grid(row=0, column=0)

# Area where you can enter a value
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0, column=1)

# Display field
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

# This should always be at the end of your code.
window.mainloop()

