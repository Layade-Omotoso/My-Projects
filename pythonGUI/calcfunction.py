import tkinter as tk


class CalcFunction():
     def __init__(self):
         pass
     
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
                