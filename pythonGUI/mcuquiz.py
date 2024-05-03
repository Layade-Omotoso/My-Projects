import tkinter as tk
from tkinter import ttk
from random import randrange as rd
from PIL import ImageTk, Image

class Quiz:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('New Horizons - McPherson Quiz')
        self.root.geometry('500x350')
        self.root.resizable(False,False)

        self.captionFrame = tk.Frame(self.root)
        self.img = Image.open('mcu.jpg')
        self.image = self.img.resize((50,55))
        self.photo = ImageTk.PhotoImage(self.image)
        tk.Label(self.captionFrame, image=self.photo).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.label = tk.Label(self.captionFrame, text='New Horizons - McPherson University\n Seriki-Sotayo, Ogun State.', font=('Arial',14)).grid(row=0, column=1, sticky=tk.E, pady=5, padx=40)
        self.captionFrame.pack()
        tk.Label(text='..............................................................................................................................................................\n').pack(fill='x')

        self.frame = tk.Frame(self.root)
        self.pnframe = tk.Frame(self.root)

        self.fontStyle = ('Arial',12)
        self.fontStyle2 = ('Arial',11)

        self.score = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0 
        self.a5 = 0

        self.sn = 0
        self.next()
        self.pBtn = tk.Button(self.pnframe, text='Previous', font=('Arial',11),  background='green', foreground='white', width=10, command=self.previous).grid(row=1, column=0)
        self.nBtn = tk.Button(self.pnframe, text='Next', font=('Arial',11),  background='green', foreground='white', width=10, command=self.next).grid(row=1, column=1, padx=5)
        self.sBtn = tk.Button(self.pnframe, text='End Exam', font=('Arial',11),  background='blue', foreground='white', width=10, command=self.scores).grid(row=1, column=2, padx=5)
        self.pnframe.pack(fill='x', side='bottom', padx=90, pady=10)

        self.root.mainloop()
    def ans1(self):
        self.a1=1

    def ans2(self):
        self.a2=1

    def ans3(self):
        self.a3=1

    def ans4(self):
        self.a4=1

    def ans5(self):
        self.a5=1
        
    def scores(self):
        self.score = self.a1 + self.a2 + self.a3 + self.a4 + self.a5
        print(self.score)

    def previous(self):
        # self.scores()
        # print(self.score)
        if(self.sn >1): 
            self.sn -= 1
        self.frame.destroy()
        # self.rand = rd(1,6)
        if(self.sn==1):
            self.question1()
        elif(self.sn==2):
            self.question2()
        elif(self.sn==3):
            self.question3()
        elif(self.sn==4):
            self.question4()
 
        # else: 
        #     self.question5()
        # if(self.rand==1):
        #     self.question1()
        # elif(self.rand==2):
        #     self.question2()
        # elif(self.rand==3):
        #     self.question3()
        # elif(self.rand==4):
        #     self.question4()
        # else: 
        #     self.question5()

    def next(self):
        # self.scores()
        # print(self.score)
        if(self.sn <5): 
            self.sn += 1
        self.frame.destroy()
        # self.rand = rd(1,6)
        if(self.sn==1):
            self.question1()
        elif(self.sn==2):
            self.question2()
        elif(self.sn==3):
            self.question3()
        elif(self.sn==4):
            self.question4()
        else: 
            self.question5()
       
        # self.rand = rd(1,6)
        # if(self.rand==1):
        #     self.question1()
        # elif(self.rand==2):
        #     self.question2()
        # elif(self.rand==3):
        #     self.question3()
        # elif(self.rand==4):
        #     self.question4()
        # else: 
        #     self.question5()


    def question1(self):
        self.gname = tk.StringVar(value='q1')
        self.frame = tk.Frame(self.root)
        self.qLabel1 = tk.Label(self.frame, text=str(self.sn)+'. ', font=self.fontStyle).grid(row=0, column=0)
        self.qLabel1 = tk.Label(self.frame, text='Who is the President of Nigeria?', font=self.fontStyle).grid(row=0, column=1)
        tk.Radiobutton(self.frame, text='A.   Omotoso Akintola', value='q1a', font=self.fontStyle2, variable=self.gname).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='B.   Muhammed Asiwaju', value='q1b', font=self.fontStyle2, variable=self.gname).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='C.   Hammed Tinubu', value='q1c', font=self.fontStyle2, command=self.ans1, variable=self.gname).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='D.   Charles Temitope', value='q1d', font=self.fontStyle2, variable=self.gname).grid(row=4, column=1, sticky=tk.W)
        self.frame.pack(fill='x')

    def question2(self):
        self.gname = tk.StringVar(value='q2')
        self.frame = tk.Frame(self.root)
        self.qLabel1 = tk.Label(self.frame, text=str(self.sn)+'. ', font=self.fontStyle).grid(row=0, column=0)
        self.qLabel1 = tk.Label(self.frame, text='Which state is McPherson University located?', font=self.fontStyle).grid(row=0, column=1)
        tk.Radiobutton(self.frame, text='A.   Osun State', value='q2a', font=self.fontStyle2, variable=self.gname).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='B.   Oyo State', value='q2b', font=self.fontStyle2, variable=self.gname).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='C.   Ekiti State', value='q2c', font=self.fontStyle2, variable=self.gname).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='D.   Ogun State', value='q2d', command=self.ans2, font=self.fontStyle2, variable=self.gname).grid(row=4, column=1, sticky=tk.W)
        self.frame.pack(fill='x')


    def question3(self):
        self.gname = tk.StringVar(value='q3')
        self.frame = tk.Frame(self.root)
        self.qLabel1 = tk.Label(self.frame, text=str(self.sn)+'. ', font=self.fontStyle).grid(row=0, column=0)
        self.qLabel1 = tk.Label(self.frame, text='How many states are in Nigeria?', font=self.fontStyle).grid(row=0, column=1)
        tk.Radiobutton(self.frame, text='A.   29', value='q3a', font=self.fontStyle2, variable=self.gname).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='B.   30', value='q3b', font=self.fontStyle2, variable=self.gname).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='C.   36', value='q3c', font=self.fontStyle2, command=self.ans3, variable=self.gname).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='D.   39', value='q3d', font=self.fontStyle2, variable=self.gname).grid(row=4, column=1, sticky=tk.W)
        self.frame.pack(fill='x')

    def question4(self):
        self.gname = tk.StringVar(value='q4')
        self.frame = tk.Frame(self.root)
        self.qLabel1 = tk.Label(self.frame, text=str(self.sn)+'. ', font=self.fontStyle).grid(row=0, column=0)
        self.qLabel1 = tk.Label(self.frame, text='What is the state capital of Lagos', font=self.fontStyle).grid(row=0, column=1)
        tk.Radiobutton(self.frame, text='A.   Osogbo', value='q4a', font=self.fontStyle2, variable=self.gname).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='B.   Ikeja', value='q4b', font=self.fontStyle2, command=self.ans4, variable=self.gname).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='C.   Victoria Island', value='q4c', font=self.fontStyle2, variable=self.gname).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='D.   Abuja', value='q4d', font=self.fontStyle2, variable=self.gname).grid(row=4, column=1, sticky=tk.W)
        self.frame.pack(fill='x')

    def question5(self):
        self.gname = tk.StringVar(value='q5')
        self.frame = tk.Frame(self.root)
        self.qLabel1 = tk.Label(self.frame, text=str(self.sn)+'. ', font=self.fontStyle2).grid(row=0, column=0)
        self.qLabel1 = tk.Label(self.frame, text='Who is the Governor of Oyo State', font=self.fontStyle).grid(row=0, column=1)
        tk.Radiobutton(self.frame, text='A.   Fashola Akinbola', value='q5a', font=self.fontStyle2, variable=self.gname).grid(row=1, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='B.   Seyi Makinde', value='q5b', command=self.ans5, font=self.fontStyle2, variable=self.gname).grid(row=2, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='C.   Hammed Tinuola', value='q5c', font=self.fontStyle2, variable=self.gname).grid(row=3, column=1, sticky=tk.W)
        tk.Radiobutton(self.frame, text='D.   Akintunde Bakare', value='q5d', font=self.fontStyle2, variable=self.gname).grid(row=4, column=1, sticky=tk.W)
        self.frame.pack(fill='x')

Quiz()