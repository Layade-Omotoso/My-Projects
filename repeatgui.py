import tkinter as tk
from tkinter import messagebox

class ReviewGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Review GUI')
        self.root.protocol('WM_DELETE_WINDOW', self.closeit)

        self.frame = tk.Frame(self.root)

        self.label = tk.Label(self.frame, text='Full Name', font=('Arial',12))
        self.label.grid(row=0, column=0)

        self.txtbox = tk.Entry(self.frame, font=('Arial',11))
        self.txtbox.grid(row=0, column=1)

        self.btn = tk.Button(self.frame, text='Greet', font=('Arial',12), command=self.greet)
        self.btn.grid(row=0, column=2)

        # self.radio1 = tk.Radiobutton(self.frame, text='Married')
        # self.radio1.grid(row=1, column=0)
        # self.radio2 = tk.Radiobutton(self.frame, text='Single')
        # self.radio2.grid(row=1, column=1)
        # self.radio3 = tk.Radiobutton(self.frame,  text='Divorced')
        # self.radio3.grid(row=1, column=2)

        self.frame.pack(fill='x', padx=10, pady=10)

        self.root.mainloop()
    
    def greet(self):
        mess = 'Good morning ' + self.txtbox.get()
        messagebox.showinfo(title='Greeting', message=mess)
    
    def closeit(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you want to quit?'):
            self.root.destroy()

ReviewGUI()