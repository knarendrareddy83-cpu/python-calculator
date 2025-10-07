import tkinter as tk
a=""
def add(symbol):
    global a
    a +=str(symbol)
    text.delete(1.0,"end")
    text.insert(1.0,a)
def calculate():
    global a
    try:
        result=str(eval(a))
        a=""
        text.delete(1.0,"end")
        text.insert(1.0,result)
    except:
        clear()
        text.insert(1.0,"error")
def clear():
    global a
    a=""
    text.delete(1.0,"end")
        
root=tk.Tk()
root.title("GUI CALCULATOR")
text=tk.Text(root,height=5)
text.grid(columnspan=5)

bt=tk.Button(root,text="1", command=lambda: add(1))
bt.grid(row=2,column=1)
bt=tk.Button(root,text="2", command=lambda: add(3))
bt.grid(row=2,column=2)
bt=tk.Button(root,text="3", command=lambda: add(3))
bt.grid(row=2,column=3)
bt=tk.Button(root,text="4", command=lambda: add(4))
bt.grid(row=3,column=1)
bt=tk.Button(root,text="5", command=lambda: add(5))
bt.grid(row=3,column=2)
bt=tk.Button(root,text="6", command=lambda: add(6))
bt.grid(row=3,column=3)
bt=tk.Button(root,text="7", command=lambda: add(7))
bt.grid(row=4,column=1)
bt=tk.Button(root,text="8", command=lambda: add(8))
bt.grid(row=4,column=2)
bt=tk.Button(root,text="9", command=lambda: add(9))
bt.grid(row=4,column=3)
bt=tk.Button(root,text="0", command=lambda: add(0))
bt.grid(row=5,column=1)
bt=tk.Button(root,text="+", command=lambda: add("+"))
bt.grid(row=5,column=2)
bt=tk.Button(root,text="-", command=lambda: add("-"))
bt.grid(row=5,column=3)
bt=tk.Button(root,text="*", command=lambda: add("*"))
bt.grid(row=6,column=1)
bt=tk.Button(root,text="/", command=lambda: add("/"))
bt.grid(row=6,column=2)
bt=tk.Button(root,text="=", command=calculate)
bt.grid(row=6,column=3)
bt=tk.Button(root,text="C", command=clear)
bt.grid(row=7,column=1)



root.mainloop()
