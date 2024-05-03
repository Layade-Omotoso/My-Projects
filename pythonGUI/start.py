import tkinter as tk
from random import randrange as rd

class Quiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('New Horizons - McPherson Quiz')
        self.root.geometry('500x300')
        self.root.resizable(False,False)
        self.frame = tk.Frame(self.root)

        label = tk.Label(self.root, text='New Horizons - McPherson University\n Seriki-Sotayo, Ogun State.', font=('Arial',13)).pack(pady=20)
        # label.grid(row=0, columnspan=2, pady=10, padx=100)


        self.nBtn = tk.Button(self.frame, text='Start', font=('Arial',11),  background='blue', foreground='white', width=20, command=self.nextQ)
        self.nBtn.pack(padx=20, pady=50)

        self.frame.pack(fill='x')
        self.root.mainloop()

    def nextQ(self):
        self.root.destroy()
        import mcuquiz

Quiz()