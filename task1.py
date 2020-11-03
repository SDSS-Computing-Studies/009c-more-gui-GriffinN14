import tkinter as tk
from tkinter import *
import math
window = tk.Tk()

answer = StringVar()



tripic = PhotoImage(file="triangle.png")
pic = tk.Label(window, image=tripic)
entrya = tk.Entry(window, width=8, borderwidth=3)
entryb = tk.Entry(window, width=8, borderwidth=3)
entryc = tk.Entry(window, width=8, borderwidth=3)
entryh = tk.Entry(window, width=8, borderwidth=3)
text = tk.Label(window, text="Enter in as mauch information about the\ntriangle shown and i will calculate the area put 0's for unkown data")
answerdis = tk.Entry(window,textvariable=answer)

def calculate():
    a = entrya.get()
    b = entryb.get()
    c = entryc.get()
    h = entryh.get()
    a = int(a)
    b = int(b)
    c = int(c)
    h = int(h)
    if not h == 0 and not c == 0:
        A = c*h/2
        answer.set(A)
    elif a != 0 and b != 0 and c != 0:
        s = (a+b+c)/2
        A = math.sqrt(s*(s-a)*(s-b)*(s-c))
        A = round(A, 1)
        answer.set(A)
    else:
        answer.set("cannot be calculated")

button = tk.Button(window, text="Calculate!", command=calculate)

entrya.place(x=180,y=90)
entryb.place(x=380,y=120)
entryc.place(x=230,y=230)
entryh.place(x=300,y=110)
pic.grid(row=1,column=1,columnspan=2)
text.grid(row=2,column=1)
button.grid(row=2,column=2)
answerdis.grid(row=3,column=1,columnspan=2)
window.mainloop()