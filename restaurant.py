from datetime import date, timedelta
import tkinter as tk
from tkinter import messagebox
from os.path import exists

class MyGUI: 
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Another GUI')
        self.root.geometry('350x600')
        
        self.align = 'right'
        self.btnframe = tk.Frame(self.root)
        self.entrylen = 7
        self.hspace = 5
        self.vspace = 50
        self.total = 0
        self.btnbgcolor='blue'
        self.btnfgcolor = 'white'
        self.btnpadx = 10
        self.todayStr = ''     
        self.label = tk.Label(self.root, text="Food Restaurant App", font=('Arial',15)).pack(fill='x', pady=10) 
        self.initRice = tk.IntVar(value=0)
        self.initBeans = tk.IntVar(value=0)
        self.initSpag = tk.IntVar(value=0)
        self.initDodo = tk.IntVar(value=0)
        self.initMeat = tk.IntVar(value=0)
        self.initFish = tk.IntVar(value=0)
        self.initMoimoi = tk.IntVar(value=0)
        self.initEgg = tk.IntVar(value=0)
        self.initSoftd = tk.IntVar(value=0)
        self.initWater = tk.IntVar(value=0)
        self.initTotal = 0
        self.prev = 0
        self.label = tk.Label(self.btnframe, text="Rice", font=('Arial',12))
        self.label.grid(row=0, column=0, sticky=tk.W) 
        self.rice = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen, textvariable=self.initRice, justify=self.align)
        self.rice.grid(row=0, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)
        
        self.label = tk.Label(self.btnframe, text="Beans", font=('Arial',12))
        self.label.grid(row=1, column=0, sticky=tk.W)
        self.beans = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initBeans, justify=self.align)
        self.beans.grid(row=1, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)
 
        self.label = tk.Label(self.btnframe, text="Spagetti", font=('Arial',12))
        self.label.grid(row=2, column=0, sticky=tk.W)
        self.spag = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initSpag, justify=self.align)
        self.spag.grid(row=2, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Dodo", font=('Arial',12))
        self.label.grid(row=3, column=0, sticky=tk.W)
        self.dodo = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initDodo, justify=self.align)
        self.dodo.grid(row=3, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Meat", font=('Arial',12))
        self.label.grid(row=4, column=0, sticky=tk.W)
        self.meat = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initMeat, justify=self.align)
        self.meat.grid(row=4, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Fish", font=('Arial',12))
        self.label.grid(row=5, column=0, sticky=tk.W)
        self.fish = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initFish, justify=self.align)
        self.fish.grid(row=5, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Moin-Moin", font=('Arial',12))
        self.label.grid(row=6, column=0, sticky=tk.W)
        self.moinmoin = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initMoimoi, justify=self.align)
        self.moinmoin.grid(row=6, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Egg", font=('Arial',12))
        self.label.grid(row=7, column=0, sticky=tk.W)
        self.egg = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initEgg, justify=self.align)
        self.egg.grid(row=7, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Soft Drink", font=('Arial',12))
        self.label.grid(row=8, column=0, sticky=tk.W)
        self.softd = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initSoftd, justify=self.align)
        self.softd.grid(row=8, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.label = tk.Label(self.btnframe, text="Water", font=('Arial',12))
        self.label.grid(row=9, column=0, sticky=tk.W)
        self.water = tk.Entry(self.btnframe, font=('Arial',12), width=self.entrylen,  textvariable=self.initWater, justify=self.align)
        self.water.grid(row=9, column=1, padx=self.vspace, pady=self.hspace, sticky=tk.E)

        self.totalbtn = tk.Button(self.btnframe, text="Calculate", font=('Arial',12), bg=self.btnbgcolor, fg=self.btnfgcolor, padx=self.btnpadx, command=self.showTotal).grid(row=10, column=1, columnspan=2, pady=5)
        self.label = tk.Label(self.btnframe, text="TOTAL", font=('Arial',15), pady=10)
        self.label.grid(row=11, column=0, sticky=tk.W+tk.E)
        self.totalbox = tk.Entry(self.btnframe, font=('Arial',20), width=self.entrylen,  textvariable=self.initTotal, bg='#ccf', justify=self.align)
        self.totalbox.grid(row=11, column=1, sticky=tk.W+tk.E)

        tk.Button(self.btnframe, text="-1", font=('Arial',12), bg='red', fg=self.btnfgcolor, command=self.minus1).grid(row=12, column=0, pady=5, sticky=(tk.E))
        tk.Button(self.btnframe, text="+1", font=('Arial',12), bg='green', fg=self.btnfgcolor, command=self.plus1).grid(row=12, column=2, pady=5, sticky=(tk.E))
        self.allsales = tk.Button(self.btnframe, text="Today's Sales", font=('Arial',12), bg=self.btnbgcolor, fg=self.btnfgcolor, padx=self.btnpadx, command=self.dailyTotal).grid(row=12, column=1, pady=5, sticky=(tk.W,tk.E))
        self.dateLabel = tk.Label(self.root, text=self.todayStr, font=('Arial',12), pady=10)
        self.dateLabel.pack(side='bottom')
        self.btnframe.pack(fill='x', padx=20, pady=20)
        self.root.protocol("WM_DELETE_WINDOW", self.closing)
        self.root.mainloop()

    def minus1(self):
        self.prev+=1
        self.dailyTotal()

    def plus1(self):
        self.prev-=1
        self.dailyTotal()


    def showTotal(self):
        today = date.today()
        self.todayStr = str(today)+'.txt'
        sum = str(int(self.initRice.get())+int(self.initBeans.get())+int(self.initSpag.get())+int(self.initDodo.get())+int(self.initMeat.get())+int(self.initFish.get())+int(self.initMoimoi.get())+int(self.initEgg.get())+int(self.initSoftd.get())+int(self.initWater.get()))
        self.initTotal = sum
        with open(self.todayStr,'a') as w:
            sum1 = sum+'\n'
            w.writelines(sum1)  
        self.totalbox.delete(0,tk.END) 
        self.totalbox.config(background='#ccf')
        self.totalbox.insert(tk.INSERT, sum)

        self.startit()


    def dailyTotal(self):
        self.todayStr = str(date.today()-timedelta(days=self.prev))+'.txt'   
        if exists(self.todayStr):
            with open(self.todayStr) as r:
                self.total = 0
                self.content = r.readlines()
                self.tl = len(self.content)
                for a in range(0,self.tl):
                    self.total += int(self.content[a])
            self.totalbox.config(background='#cfc')
            self.totalbox.delete(0,tk.END) 
            self.totalbox.insert(tk.INSERT, self.total)
            self.dateLabel.config(text=(self.todayStr[0:10]))
        else:
            self.totalbox.config(background='#cfc')
            self.totalbox.config(justify='center')
            self.totalbox.delete(0,tk.END) 
            self.totalbox.insert(tk.INSERT,'No Sales')
            self.dateLabel.config(text=(self.todayStr[0:10]))

    def startit(self):
        self.rice.delete(0,tk.END)
        self.beans.delete(0,tk.END)
        self.spag.delete(0,tk.END)        
        self.dodo.delete(0,tk.END)        
        self.meat.delete(0,tk.END)    
        self.fish.delete(0,tk.END)
        self.moinmoin.delete(0,tk.END)
        self.egg.delete(0,tk.END)
        self.softd.delete(0,tk.END)
        self.water.delete(0,tk.END)
       
        self.rice.insert(0,'0')
        self.beans.insert(0,'0')
        self.spag.insert(0,'0')
        self.dodo.insert(0,'0')
        self.meat.insert(0,'0')
        self.fish.insert(0,'0')
        self.moinmoin.insert(0,'0')
        self.egg.insert(0,'0')
        self.softd.insert(0,'0')
        self.water.insert(0,'0')
        self.rice.focus_set()


    def closing(self):
        if messagebox.askyesno(title='Quit?', message="Do you really want to quit?"):
            self.root.destroy()




MyGUI()