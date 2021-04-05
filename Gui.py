"""from tkinter import *
                        #creating the application main window.
top = Tk()
                         #Entering the event main loop
top.mainloop()
"""


"""from tkinter import *

top = Tk()

top.geometry("200x200")

checkvar1 = IntVar()

checkvar2 = IntVar()

checkvar3 = IntVar()

chkbtn1 = Checkbutton(top, text = "C", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10)

chkbtn2 = Checkbutton(top, text = "C++", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10)

chkbtn3 = Checkbutton(top, text = "Java", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)

chkbtn1.pack()

chkbtn2.pack()

chkbtn3.pack()

top.mainloop()"""

"""import tkinter as tk
from functools import partial
"""
"""
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result = %d" % result)
    return

root = tk.Tk()
root.geometry('400x200+100+200')

root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result = partial(call_result, labelResult, number1, number2)

buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)

root.mainloop()"""

"""from tkinter import *
from tkinter import messagebox

top = Tk()

top.geometry("200x100")

def fun():
    messagebox.showerror("error","Error")
def gun():
    messagebox.showinfo("Hello ", "blue Button clicked")
def nun():
    messagebox.askquestion("Confirm","Are you sure?")
def mun():
    messagebox.showinfo("Hello", "yellow Button clicked")
b1 = Button(top,text = "LEFT",command = fun,activeforeground = "red",activebackground = "pink",pady=10)

b2 = Button(top, text = "RIGHT",command = gun,activeforeground = "blue",activebackground = "pink",pady=10)

b3 = Button(top, text = "TOP",command = nun,activeforeground = "green",activebackground = "pink",pady = 10)

b4 = Button(top, text = "BOTTOM",command = mun,activeforeground = "yellow",activebackground = "pink",pady = 10)

b1.pack(side = LEFT)

b2.pack(side = RIGHT)

b3.pack(side = TOP)

b4.pack(side = BOTTOM)

"""



"""top.mainloop()"""


"""from tkinter import *

top = Tk()
sb = Scrollbar(top)
sb.pack(side = RIGHT, fill = Y)

mylist = Listbox(top, yscrollcommand = sb.set )

for line in range(50):
    mylist.insert(END, "Number " + str(line))

mylist.pack( side = LEFT )
sb.config( command = mylist.yview )

mainloop()
"""
