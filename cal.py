from tkinter import *

root=Tk()
root.title("cal")
root.geometry("185x165")

equation_text = ""
equation_label = StringVar()

def btn_click(number):
    global equation_text
    equation_text = equation_text + str(number)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text=total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text=""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text=""

def clear():
    global equation_text
    equation_label.set("")
    equation_text=""

label=Label(textvariable=equation_label, bg="white", width=22)
label.pack()

btnframe=Frame()
btnframe.pack()

btnframe.columnconfigure([0,1,2,3], minsize=40)
btn1 = Button(btnframe, text="1", command=lambda: btn_click(1))
btn2 = Button(btnframe, text="2", command=lambda: btn_click(2))
btn3 = Button(btnframe, text="3", command=lambda: btn_click(3))
btn4 = Button(btnframe, text="4", command=lambda: btn_click(4))
btn5 = Button(btnframe, text="5", command=lambda: btn_click(5))
btn6 = Button(btnframe, text="6", command=lambda: btn_click(6))
btn7 = Button(btnframe, text="7", command=lambda: btn_click(7))
btn8 = Button(btnframe, text="8", command=lambda: btn_click(8))
btn9 = Button(btnframe, text="9", command=lambda: btn_click(9))
btn0 = Button(btnframe, text="0", command=lambda: btn_click(0))
btn1.grid(row=1, column=0, sticky="nsew")
btn2.grid(row=1, column=1, sticky="nsew")
btn3.grid(row=1, column=2, sticky="nsew")
btn4.grid(row=2, column=0, sticky="nsew")
btn5.grid(row=2, column=1, sticky="nsew")
btn6.grid(row=2, column=2, sticky="nsew")
btn7.grid(row=3, column=0, sticky="nsew")
btn8.grid(row=3, column=1, sticky="nsew")
btn9.grid(row=3, column=2, sticky="nsew")
btn0.grid(row=4, columnspan=2, sticky="nsew")

clean = Button(btnframe, text="clear", command=clear)
clean.grid(row=0, columnspan=3,sticky="nesw")
plus = Button(btnframe, text="+", command=lambda: btn_click("+"))
plus.grid(row=0, column=3,sticky="nesw")
minus = Button(btnframe, text="-", command=lambda: btn_click("-"))
minus.grid(row=1, column=3,sticky="nesw")
multiply = Button(btnframe, text="*", command=lambda: btn_click("*"))
multiply.grid(row=2, column=3,sticky="nesw")
divide = Button(btnframe, text="/", command=lambda: btn_click("/"))
divide.grid(row=3, column=3,sticky="nesw")
decimal = Button(btnframe, text=".", command=lambda: btn_click("."))
decimal.grid(row=4, column=2,sticky="nesw")
equal = Button(btnframe, text="=", command=equals)
equal.grid(row=4, column=3,sticky="nesw")

root.mainloop()
