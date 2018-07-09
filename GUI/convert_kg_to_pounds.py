#GUI to take kg weight as input and convert to grams, poinds and ounces

from tkinter import *

MAX_ROWS = 36
FONT_SIZE = 10 # (pixels)

COLORS = ['PeachPuff2']

window=Tk()

window.tk_setPalette(COLORS)

def set_values():
#   Get the value from the e1_value string StringVar function
    kg=float(e2_value.get())
    grams=kg*1000
    pounds=kg*2.20462
    ounces=kg*35.274
#   Clear up any previous values
    t1.delete("1.0", END)
    t2.delete("1.0", END)
    t3.delete("1.0", END)
#   Now insert the value retrieved into the display fields - at the End)
    t1.insert(END,round(grams,1))
    t2.insert(END,round(pounds,4))
    t3.insert(END,round(ounces,2))
        
#Label
e1=Label(window,text="Kg",height=1,width=22)
e1.grid(row=0, column=0)

# Area where you can enter a value - Get the KG value
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0, column=1)

# Button
b1=Button(window,text="Convert", command=set_values)
b1.grid(row=0, column=2)

# Display field 1 (grams)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=0)

# Display field 2 (pounds)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=1)

# Display field 3 (ounces)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=2)

# This should always be at the end of your code.
window.mainloop()

