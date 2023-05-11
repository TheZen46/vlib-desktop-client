from tkinter import *
from tkinter import ttk

fds = Tk()
fds.title('Name This Window')
fds.configure(bg="#ffffff")
notebook = ttk.Notebook(fds)

tab1 = Frame(notebook, padx= 52, pady= 25, width= 34)
tab2 = Frame(notebook, padx= 55, pady= 29, width= 24)

notebook.add(tab1, text='dasds')
notebook.add(tab2, text='dasdsa2')
notebook.pack()

label = Label(tab1, text = 'Enter The Text')
label.grid(row = 50, column = 25)
button = Button(tab2, text = 'Click me !', 
                borderwidth=0, 
                bg="#272932", 
                relief=SUNKEN, 
                command=lambda: print('button clicked')
                )

calc = OptionMenu(tab1, int, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
calc.grid(row = 20, column = 30)

dsf = (tab2)
dsf.grid(row = 15, column = 9)

button.grid(row = 55, 
            column = 25)


fds.mainloop()