import tkinter as tk
from tkinter import *

def add_to_expression(symbol):
    global exp
    exp+=str(symbol)
    var.set(exp)
def clear_expression():
    global exp
    exp=""
    var.set("")
def evaluate_expression():
    global exp
    try:
        result = str(eval(exp))
        var.set(result)
        exp = result
    except Exception:
        var.set("Error")
        exp = ""



root=tk.Tk()
root.title("Calculator")
root.geometry("444x544")
root.maxsize(444,544)
root.configure(bg="black")
root.resizable(False,False)
root.wm_iconbitmap("cal.ico")

exp=""
var=tk.StringVar()
val=tk.Entry(root, bg="#2d2d2d",textvariable=var,bd=0,font=" lucida 57  bold",fg="white",justify="right")
val.grid(row=0,column=0,columnspan=4,padx=10,pady=10,ipady=15,sticky="we")

bttnft=(" lucida 57  bold")
btn_bg = "#333333"
bttnfg="white"
btn_active = "#555555"

def make_button(text,row,col,cmd,bg=btn_bg):
    btn=tk.Button(root,text=text,bg=bg,activebackground=btn_active,relief="flat",activeforeground="white",font=bttnft,width=5,height=2,command=cmd)
    btn.grid(row=row,column=col,padx=5,pady=5)

make_button("C", 1, 0, clear_expression, bg="#ff5e5e")
make_button("+/-", 1, 1, lambda: add_to_expression("-"))
make_button("%", 1, 2, lambda: add_to_expression("%"))
make_button("÷", 1, 3, lambda: add_to_expression("/"), bg="#ff9500")

make_button("7", 2, 0, lambda: add_to_expression(7))
make_button("8", 2, 1, lambda: add_to_expression(8))
make_button("9", 2, 2, lambda: add_to_expression(9))
make_button("×", 2, 3, lambda: add_to_expression("*"), bg="#ff9500")

make_button("4", 3, 0, lambda: add_to_expression(4))
make_button("5", 3, 1, lambda: add_to_expression(5))
make_button("6", 3, 2, lambda: add_to_expression(6))
make_button("-", 3, 3, lambda: add_to_expression("-"), bg="#ff9500")

make_button("1", 4, 0, lambda: add_to_expression(1))
make_button("2", 4, 1, lambda: add_to_expression(2))
make_button("3", 4, 2, lambda: add_to_expression(3))
make_button("+", 4, 3, lambda: add_to_expression("+"), bg="#ff9500")

make_button("0", 5, 0, lambda: add_to_expression(0))
make_button(".", 5, 1, lambda: add_to_expression("."))
make_button("=", 5, 2, evaluate_expression, bg="#00cc66")

root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure((0, 1, 2, 3), weight=1)
root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)



root.mainloop()