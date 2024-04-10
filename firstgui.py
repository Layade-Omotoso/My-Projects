import tkinter as tk
from tkinter import messagebox

class MyGUI: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Another GUI')
        
        
        self.btnframe = tk.Frame(self.root)
       
        
        self.label = tk.Label(self.btnframe, text="Rice", font=('Arial',12))
        self.label.grid(row=0, column=0, sticky=tk.W)
        
        self.rice = tk.Entry(self.btnframe, font=('Arial',12))
        self.rice.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        self.label = tk.Label(self.btnframe, text="Beans", font=('Arial',12))
        self.label.grid(row=1, column=0, sticky=tk.W)
        
        self.beans = tk.Entry(self.btnframe, font=('Arial',12))
        self.beans.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
             
        self.totalbtn = tk.Button(self.btnframe, text="Calculate", font=('Arial',12), command=self.showTotal)
        self.totalbtn.grid(row=2, column=1, pady=10)
        
        self.btnframe.pack(fill='x', padx=20, pady=20)
        self.root.protocol("WM_DELETE_WINDOW", self.closing)
        self.root.mainloop()
        
    def showTotal(self):
        total = 'Total is N' + str(float(self.rice.get())+float(self.beans.get()))
        print(total)        
        messagebox.showinfo(title='Total Amount is ', message = total)
        
    def closing(self):
        if messagebox.askyesno(title='Quit?', message="Do you really want to quit?"):
            self.root.destroy()
            import calc


MyGUI()