import tkinter as tk
root = tk.Tk() #CREATES BASE OF GUI
root.title("Calculator")
root.geometry("350x400")
entry=tk.Entry(root, width=20, font=("Aerial", 24))
entry.grid(row=0, column=0, columnspan=4)
def press(value):
    current = entry.get()
    if value in "+-*/":
        if current and current[-1] in "+-*/":
            entry.delete(len(current)-1, tk.END)   # delete last operator
            entry.insert(tk.END, value)            # insert new operator
        else:
            entry.insert(tk.END, value)
    else:
        entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)
def calculate():
    expression=entry.get()
    result=eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)
button7=tk.Button(root, text="7", width=5, height=2, command=lambda:press("7"))
button7.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
button8=tk.Button(root, text="8", width=5, height=2, command=lambda:press("8"))
button8.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
button9=tk.Button(root, text="9", width=5, height=2, command=lambda:press("9"))
button9.grid(row=1, column=2, sticky="nsew", padx=0, pady=0)
button4=tk.Button(root, text="4", width=5, height=2, command=lambda:press("4"))
button4.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)
button5=tk.Button(root, text="5", width=5, height=2, command=lambda:press("5"))
button5.grid(row=2, column=1, sticky="nsew", padx=0, pady=0)
button6=tk.Button(root, text="6", width=5, height=2, command=lambda:press("6"))
button6.grid(row=2, column=2, sticky="nsew", padx=0, pady=0)
button1=tk.Button(root, text="1", width=5, height=2, command=lambda:press("1"))
button1.grid(row=3, column=0, sticky="nsew", padx=0, pady=0)
button2=tk.Button(root, text="2", width=5, height=2, command=lambda:press("2"))
button2.grid(row=3, column=1, sticky="nsew", padx=0, pady=0)
button3=tk.Button(root, text="3", width=5, height=2, command=lambda:press("3"))
button3.grid(row=3, column=2, sticky="nsew", padx=0, pady=0)
button0=tk.Button(root, text="0", width=5, height=2, command=lambda:press("0"))
button0.grid(row=4, column=1, sticky="nsew", padx=0, pady=0)
operator_div=tk.Button(root, text="/", width=5, height=2, command=lambda:press("/"))
operator_div.grid(row=1, column=3, sticky="nsew", padx=0, pady=0)
operator_mult=tk.Button(root, text="*", width=5, height=2, command=lambda:press("*"))
operator_mult.grid(row=2, column=3, sticky="nsew", padx=0, pady=0)
operator_sub=tk.Button(root, text="-", width=5, height=2, command=lambda:press("-"))
operator_sub.grid(row=3, column=3, sticky="nsew", padx=0, pady=0)
operator_add=tk.Button(root, text="+", width=5, height=2, command=lambda:press("+"))
operator_add.grid(row=4, column=3, sticky="nsew", padx=0, pady=0)
operator_point=tk.Button(root, text=".", width=5, height=2, command=lambda:press("."))
operator_point.grid(row=4, column=0, sticky="nsew", padx=0, pady=0)
operator_equal=tk.Button(root, text="=", width=5, height=2, command=calculate)
operator_equal.grid(row=4, column=2, sticky="nsew", padx=0, pady=0)
clear1=tk.Button(root, text="C",width=5, height=2, command=clear)
clear1.grid(row=5, column=0, sticky="nsew", padx=0, pady=0)
root.mainloop()