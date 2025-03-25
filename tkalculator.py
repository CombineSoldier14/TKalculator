from tkinter import *

m = Tk()

i = ""

def add(num: int):
    global i
    if(type(i) != str or i == "Error"):
        i = ""
    i += str(num)

def calculate():
    global i
    try:
        i = eval(i)
    except:
        i = "Error"

def erase():
    global i
    if(type(i) != str or i == "Error"):
        i = ""
    else:
        i = i[:-1]

m.title("TKalculator v1.0")

T = Text(m, height=2, width=20, font=("Monospace", 10))
T.config(background="yellow")
T.grid(row=0, column=0, columnspan=4)

version = Label(m, text="© 2025 CombineSoldier14", font=("Arial", 8))
version.grid(row=6, column=0, columnspan=3)

one = Button(m, text="1", command=lambda: add(1))
two = Button(m, text="2", command=lambda: add(2))
three = Button(m, text="3", command=lambda: add(3))
four = Button(m, text="4", command=lambda: add(4))
five = Button(m, text="5", command=lambda: add(5))
six = Button(m, text="6", command=lambda: add(6))
seven = Button(m, text="7", command=lambda: add(7))
eight = Button(m, text="8", command=lambda: add(8))
nine = Button(m, text="9", command=lambda: add(9))
zero = Button(m, text="0", command=lambda: add(0))
plus = Button(m, text="+", command=lambda: add("+"))
minus = Button(m, text="-", command=lambda: add("-"))
multiply = Button(m, text="*", command=lambda: add("*"))
divide = Button(m, text="/", command=lambda: add("/"))
equals = Button(m, text="=", command=lambda: calculate())
openParenthesis = Button(m, text="(", command=lambda: add("("))
closeParenthesis = Button(m, text=")", command=lambda: add(")"))
eraseButton = Button(m, text="C", command=lambda: erase())
point = Button(m, text=".", command=lambda: add("."))

one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=1)
plus.grid(row=1, column=3)
minus.grid(row=2, column=3)
multiply.grid(row=3, column=3)
divide.grid(row=4, column=3)
equals.grid(row=4, column=2)
eraseButton.grid(row=4, column=0)
point.grid(row=5, column=3)
openParenthesis.grid(row=5, column=1)
closeParenthesis.grid(row=5, column=2)

while(True):
    T.delete("1.0", END)
    T.insert(END, i)
    m.update()

m.mainloop()