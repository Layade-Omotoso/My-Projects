import tkinter as tk
import math as mt

class Calc:
    def __init__(self):
        self.operand1 = 0.0
        self.operand2 = 0.0
        self.operator = ''
        self.root = tk.Tk()
        self.root.title('Omotoso Calculator')
        self.root.resizable(False,False)
        self.displayFont = 15
        self.buttonFont = 13
        self.advcolor = '#cfc'

        #the main frame container 
        self.frame = tk.Frame(self.root)
    
        #Components inside the grids to be added to the frame
        self.display = tk.Entry(self.frame, font=('Arial', self.displayFont), border=2, background='#ccf', justify='right')
        self.display.grid(row=0, columnspan=4, sticky=(tk.W, tk.E))
        self.display.insert(tk.END,'0')

        self.btn1 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='1', command=self.one)
        self.btn1.grid(row=1, column=0, sticky=(tk.W, tk.E))

        self.btn2 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='2',  command=self.two)
        self.btn2.grid(row=1, column=1, sticky=(tk.W, tk.E))

        self.btn3 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='3', command=self.three)
        self.btn3.grid(row=1, column=2, sticky=(tk.W, tk.E))

        self.btnsin = tk.Button(self.frame, font=('Arial', self.buttonFont), text='sin', background=self.advcolor, command=self.sinX)
        self.btnsin.grid(row=1, column=3, sticky=(tk.W, tk.E))

        self.btn4 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='4', command=self.four)
        self.btn4.grid(row=2, column=0, sticky=(tk.W, tk.E))

        
        self.btn5 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='5',  command=self.five)
        self.btn5.grid(row=2, column=1, sticky=(tk.W, tk.E))

        self.btn6 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='6',  command=self.six)
        self.btn6.grid(row=2, column=2, sticky=(tk.W, tk.E))

        self.btncos = tk.Button(self.frame, font=('Arial', self.buttonFont), text='cos',  background=self.advcolor, command=self.cosX)
        self.btncos.grid(row=2, column=3, sticky=(tk.W, tk.E))
        
        self.btn7 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='7',  command=self.seven)
        self.btn7.grid(row=3, column=0, sticky=(tk.W, tk.E))
        
        self.btn8 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='8',  command=self.eight)
        self.btn8.grid(row=3, column=1, sticky=(tk.W, tk.E))
        
        self.btn9 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='9',  command=self.nine)
        self.btn9.grid(row=3, column=2, sticky=(tk.W, tk.E))
    
        self.btntan = tk.Button(self.frame, font=('Arial', self.buttonFont), text='tan', background=self.advcolor, command=self.tanX)
        self.btntan.grid(row=3, column=3, sticky=(tk.W, tk.E))

        self.btn0 = tk.Button(self.frame, font=('Arial', self.buttonFont), text='0',  command=self.zero)
        self.btn0.grid(row=4, column=0, sticky=(tk.W, tk.E))
        
        self.btnplus = tk.Button(self.frame, font=('Arial', self.buttonFont), text='+',  foreground='red', command=self.plus)
        self.btnplus.grid(row=4, column=1, sticky=(tk.W, tk.E))

        self.btnminus = tk.Button(self.frame, font=('Arial', self.buttonFont), text='-',  foreground='red', command=self.minus)
        self.btnminus.grid(row=4, column=2, sticky=(tk.W, tk.E))

        self.btnsqr = tk.Button(self.frame, font=('Arial', self.buttonFont), text='\u221A',  background=self.advcolor, command=self.squareR)
        self.btnsqr.grid(row=4, column=3, sticky=(tk.W, tk.E))


        self.btndiv = tk.Button(self.frame, font=('Arial', self.buttonFont), text='/',  foreground='red', command=self.divideby)
        self.btndiv.grid(row=5, column=0, sticky=(tk.W, tk.E))

        self.btnprod = tk.Button(self.frame, font=('Arial', self.buttonFont), text='x',  foreground='red', command=self.times)
        self.btnprod.grid(row=5, column=1, sticky=(tk.W, tk.E))

        self.btnequ = tk.Button(self.frame, font=('Arial', self.buttonFont), text='C', foreground='blue', command=self.clear)
        self.btnequ.grid(row=5, column=2, sticky=(tk.W, tk.E))

        self.btnpwr = tk.Button(self.frame, font=('Arial', self.buttonFont), text='x\u205f', background=self.advcolor, command=self.pwr)
        self.btnpwr.grid(row=5, column=3, sticky=(tk.W, tk.E))


        self.btnequ = tk.Button(self.frame, font=('Arial', self.buttonFont), text='DEL',  foreground='white', background='red', command=self.delete)
        self.btnequ.grid(row=6, column=0, sticky=(tk.W, tk.E))

        self.btnequ = tk.Button(self.frame, font=('Arial', self.buttonFont), text='=',  foreground='white', background='blue', command=self.equals)
        self.btnequ.grid(row=6, column=1, columnspan=3, sticky=(tk.W, tk.E))

        #adding the frame to the main window
        self.frame.pack(fill='x', padx=10, pady=10)



        self.root.mainloop()
    
    def one(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'1')
        else:
            self.display.insert(tk.END,'1')

    def two(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'2')
        else:
            self.display.insert(tk.END,'2')

    def three(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'3')
        else:
            self.display.insert(tk.END,'3')

    def four(self):
        if (self.display.get().startswith('0')):            
            self.display.delete(0)
            self.display.insert(0,'4')
        else:
            self.display.insert(tk.END,'4')


    def five(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'5')
        else:
            self.display.insert(tk.END,'5')

    def six(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'6')
        else:
            self.display.insert(tk.END,'6')

    def seven(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'7')
        else:
            self.display.insert(tk.END,'7')

    def eight(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'8')
        else:
            self.display.insert(tk.END,'8')

    def nine(self):
        if (self.display.get().startswith('0')):
            self.display.delete(0)
            self.display.insert(0,'9')
        else:
            self.display.insert(tk.END,'9')

    def zero(self):
        if (not self.display.get().startswith('0')):
            self.display.insert(tk.END,'0')

    def clear(self):
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')

    def delete(self):
        if((len(self.display.get()) > 1)):
            self.display.delete(self.display.index(tk.END)-1)
        else:
            self.display.delete(0)
            self.display.insert(tk.END,'0')

    def plus(self):
        self.operand1 = float(self.display.get())
        self.operator = '+'
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')

    def minus(self):
        self.operand1 = float(self.display.get())
        self.operator = '-'
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')

    def times(self):
        self.operand1 = float(self.display.get())
        self.operator = 'x'
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')

    def divideby(self):
        self.operand1 = float(self.display.get())
        self.operator = '/'
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')

    def equals(self):
        self.operand2 = float(self.display.get())
        if(self.operator=='+'):
            ans = self.operand1 + self.operand2
            self.display.delete(0,tk.END)
            self.display.insert(tk.END,ans)
        elif(self.operator=='-'):
            ans = self.operand1 - self.operand2
            self.display.delete(0,tk.END)
            self.display.insert(tk.END,ans)

        elif(self.operator=='x'):
            ans = self.operand1 * self.operand2
            self.display.delete(0,tk.END)
            self.display.insert(tk.END,ans)

        elif(self.operator=='/'):
            ans = self.operand1 / self.operand2
            self.display.delete(0,tk.END)
            self.display.insert(tk.END,ans)

        elif(self.operator=='p'):
            ans = self.operand1 ** self.operand2
            self.display.delete(0,tk.END)
            self.display.insert(tk.END,ans)
        
    def sinX(self):
        val = mt.sin(mt.radians(int(self.display.get())))
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,val)

    def cosX(self):
        val = mt.sin(mt.radians(int(self.display.get())))
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,val)
            
    def tanX(self):
        val = mt.sin(mt.radians(int(self.display.get())))
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,val)

    def pwr(self):
        self.operand1 = int(self.display.get())
        self.operator = 'p'
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,'0')
            
    def squareR(self):
        val = mt.sqrt(int(self.display.get()))
        self.display.delete(0,tk.END)
        self.display.insert(tk.END,val)
                     
Calc()
# Working perfectly. Designed by Layade Omotoso (1/4/2024)