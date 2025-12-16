from tkinter import *

window = Tk()
window.geometry("400x320")
window.title("Calculator")

# Entry Box

e = Entry(window, width=55, borderwidth=5)
e.place(x=10, y=10, height=40)

# Button Dimensions 
btn_w = 10
btn_h = 3

clear_screen = False

# Button Functions

def click(num):
    
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

b = Button(window, text="1", width=btn_w, height=btn_h, command=lambda: click(1))
b.place(x=10, y=60)

b = Button(window, text="2", width=btn_w, height=btn_h, command=lambda: click(2))
b.place(x=100, y=60)

b = Button(window, text="3", width=btn_w, height=btn_h, command=lambda: click(3))
b.place(x=190, y=60)

b = Button(window, text="4", width=btn_w, height=btn_h, command=lambda: click(4))
b.place(x=10, y=120)

b = Button(window, text="5", width=btn_w, height=btn_h, command=lambda: click(5))
b.place(x=100, y=120)

b = Button(window, text="6", width=btn_w, height=btn_h, command=lambda: click(6))
b.place(x=190, y=120)

b = Button(window, text="7", width=btn_w, height=btn_h, command=lambda: click(7))
b.place(x=10, y=180)

b = Button(window, text="8", width=btn_w, height=btn_h, command=lambda: click(8))
b.place(x=100, y=180)

b = Button(window, text="9", width=btn_w, height=btn_h, command=lambda: click(9))
b.place(x=190, y=180)

b = Button(window, text="0", width=btn_w, height=btn_h, command=lambda: click(0))
b.place(x=100, y=240)

# Math Functions

def add():
    n1 = e.get()
    global math 
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="+", width=btn_w, height=btn_h, command=add)
b.place(x=280, y=60)    

def sub():
    n1 = e.get()
    global math 
    math = "Subtraction"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="-", width=btn_w, height=btn_h, command=sub)
b.place(x=280, y=120)    

def mul():
    n1 = e.get()
    global math 
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="*", width=btn_w, height=btn_h, command=mul)
b.place(x=280, y=180)    

def div():
    n1 = e.get()
    global math 
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text="/", width=btn_w, height=btn_h, command=div)
b.place(x=280, y=240)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    if math == "Subtraction":
        e.insert(0, i - int(n2))
    if math == "multiplication":
        e.insert(0, i * int(n2))
    if math == "division":
        e.insert(0, i / int(n2))
    
b = Button(window, text="=", width=btn_w, height=btn_h, command=equal)
b.place(x=190, y=240)

def clear():
    e.delete(0, END)

b = Button(window, text="C", width=btn_w, height=btn_h, command=clear)
b.place(x=10, y=240)

window.mainloop()