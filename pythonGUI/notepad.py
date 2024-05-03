import tempfile
import tkinter as tk
from tkinter import Menu, filedialog, colorchooser, PhotoImage
from tkinter import ttk
from tkinter import messagebox
import win32print, win32api

root = tk.Tk()
filename = tk.StringVar(value='Untitled')
root.title(f"Omotoso - {filename.get()}")
root.geometry('800x600')
root.resizable(False,False)
fg = 'black'
bg = 'red'


# Images declaration
newBtn = PhotoImage(file='assets/new.png')
openBtn = PhotoImage(file='assets/open.png')
saveBtn = PhotoImage(file='assets/save.png')
copyBtn = PhotoImage(file='assets/copy.png')
cutBtn = PhotoImage(file='assets/cut.png')
pasteBtn = PhotoImage(file='assets/paste.png')
leftBtn = PhotoImage(file='assets/left.png')
centerBtn = PhotoImage(file='assets/center.png')
rightBtn = PhotoImage(file='assets/right.png')
printBtn = PhotoImage(file='assets/print.png')
fgBtn = PhotoImage(file='assets/fg.png')
bgBtn = PhotoImage(file='assets/bg.png')

def newFile():
     if messagebox.askyesno(title='Start New?', message="Are you sure you want to start afresh?"):
        fileText.delete('1.0',tk.END)

def openFile():
    filepath = filedialog.askopenfilename(title='Select a File', filetypes=[('Text files','*.txt'), ('All Files','*.*')])
    if filepath: 
        newtitle = f"Omotoso - {filepath}"
        root.title(newtitle)
        try:
            with open(filepath,'r') as file:
                fileContent = file.read()
                fileText.delete('1.0',tk.END)
                fileText.insert(tk.END,fileContent)
        except Exception as e:
            print(str(e))
        

def saveFile(evt):
    filepath = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension='.txt', title='Untitled', filetypes=[('Text files','*.txt'), ('All Files','*.*')])  
    if filepath: 
        newtitle = f"Omotoso - {filepath}"
        root.title(newtitle)
        try:
            with open(filepath,'w') as file:
                content = fileText.get('1.0',tk.END)
                file.write(content)
        except Exception as e:
            print(str(e))
        
def saveFile():
    filepath = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension='.txt', title='Untitled', filetypes=[('Text files','*.txt'), ('All Files','*.*')])  
    if filepath: 
        newtitle = f"Omotoso - {filepath}"
        root.title(newtitle)
        try:
            with open(filepath,'w') as file:
                content = fileText.get('1.0',tk.END)
                file.write(content)
                # frame1.config(bg='#efe')
        except Exception as e:
            print(str(e))
        

def fgcolor():
    fg = colorchooser.askcolor()[1]
    if fg:
        selStart, selEnd = fileText.tag_ranges('sel')
        fileText.tag_config("start", foreground=fg)
        fileText.tag_add('start',selStart, selEnd)

def bgcolor():
    bg = colorchooser.askcolor()[1]
    if bg:
        fileText.config(background=bg)

def fontType(evt):
    fileText.config(font=(Fontcombo.get(),Sizecombo.get()))

def fontSize(evt):
    fileText.config(font=(Fontcombo.get(),Sizecombo.get()))

def printing():
    printText = fileText.get('1.0',tk.END)
    print(printText)
    filen = tempfile.mktemp('.txt')
    open(filen,'w').write(printText)
    win32api.ShellExecute(0,"printto",filen,'"%s"' % win32print.GetDefaultPrinter(),".",0)

def copyIt():
    root.clipboard_clear()
    root.clipboard_append(fileText.selection_get())
    print("Length", len(fileText.selection_get()),"\nInsertion Point", fileText.index(tk.INSERT))

def cutIt():
    root.clipboard_clear()
    root.clipboard_append(fileText.selection_get())
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.delete(selStart,selEnd)
 
def pasteIt():
    fileText.insert(fileText.index(tk.INSERT), root.selection_get(selection='CLIPBOARD'))

def left():
    fileText.tag_configure('left',justify='left')
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('left',selStart,selEnd)

def center():
    fileText.tag_configure('center',justify='center')
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('center',selStart,selEnd)

def right():
    fileText.tag_configure('right',justify='right')
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('right',selStart,selEnd)

def bold():
    fileText.tag_configure('underline',underline=True)
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('underline',selStart,selEnd)

def italic():
    fileText.tag_configure('underline',underline=True)
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('underline',selStart,selEnd)

def underline():
    fileText.tag_configure('underline',underline=True)
    selStart, selEnd = fileText.tag_ranges('sel')
    fileText.tag_add('underline',selStart,selEnd)

# Menu bar 
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='New', command=newFile, accelerator='Ctrl+N')
file_menu.add_command(label='Open', command=openFile, accelerator='Ctrl+O')
file_menu.add_command(label='Save', command=saveFile, accelerator='Ctrl+S')
file_menu.add_command(label='Save As',accelerator='Ctrl+Shift+S')
file_menu.add_separator()
file_menu.add_command(label='Print', command=printing, accelerator='Ctrl+P')
file_menu.add_separator()
file_menu.add_command(label='Close', accelerator='Ctrl+W')
file_menu.add_command(label='Exit', command=root.destroy, accelerator='Alt+F4')
menubar.add_cascade(label='File',menu=file_menu)

edit_menu = Menu(menubar, tearoff=False)
edit_menu.add_command(label='Copy', command=copyIt, accelerator='Ctrl+C')
edit_menu.add_command(label='Cut', command=cutIt, accelerator='Ctrl+X')
edit_menu.add_command(label='Paste', command=pasteIt, accelerator='Ctrl+V')
edit_menu.add_separator()
edit_menu.add_command(label='Change Case')
edit_menu.add_command(label='Bold', accelerator='Ctrl+B', command=bold)
edit_menu.add_command(label='Italic', accelerator='Ctrl+I', command=italic)
edit_menu.add_command(label='Underline', accelerator='Ctrl+U', command=underline)
edit_menu.add_separator()
edit_menu.add_command(label='Page Setup', accelerator='Alt+M')
menubar.add_cascade(label='Edit',menu=edit_menu)

formatMenu = Menu(menubar, tearoff=False)
formatMenu.add_command(label='Font Size', accelerator='Alt+F')
formatMenu.add_command(label='Font Color', command=fgcolor)
formatMenu.add_command(label='Background Color', command=bgcolor)
menubar.add_cascade(label='Format',menu=formatMenu)

helpMenu = Menu(menubar, tearoff=False)
helpMenu.add_command(label='Help', accelerator='F1')
submenu = Menu(helpMenu, tearoff=0)
submenu.add_command(label='Send feedback')
submenu.add_command(label='Product Review')
helpMenu.add_command(label='About Us')
helpMenu.add_cascade(label='Get in Touch', menu=submenu)
menubar.add_cascade(label='Help', menu=helpMenu)

# Menu Items
root.config(bg='white')
frame1 = tk.Frame(root)
frame1.config(bg='white')
tk.Button(frame1, padx=5, image=newBtn, command=newFile).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=openBtn, command=openFile).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=saveBtn, command=saveFile).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=printBtn, command=printing).pack(side=tk.LEFT)
tk.Button(frame1, padx=10, image=copyBtn, command=copyIt).pack(side=tk.LEFT)
tk.Button(frame1, padx=10, image=cutBtn, command=cutIt).pack(side=tk.LEFT)
tk.Button(frame1, padx=10, image=pasteBtn, command=pasteIt).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=fgBtn, command=fgcolor).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=bgBtn, command=bgcolor).pack(side=tk.LEFT)
tk.Button(frame1, padx=5, image=leftBtn, command=left).pack(side=tk.LEFT)
tk.Button(frame1, padx=10, image=centerBtn, command=center).pack(side=tk.LEFT)
tk.Button(frame1, padx=10, image=rightBtn, command=right).pack(side=tk.LEFT)
frame1.pack(fill='x', side='top', pady=2)

fsize = tk.IntVar()
Sizecombo = ttk.Combobox(frame1, width=5, textvariable=fsize, height=9)
Sizecombo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20)
Sizecombo.current(newindex=4)
Sizecombo.bind('<<ComboboxSelected>>', fontSize)
Sizecombo.bind("<Key>", fontSize)
Sizecombo.pack(side='right', padx=5)

ftype = tk.StringVar()
Fontcombo = ttk.Combobox(frame1, width=20,values=['Arial','Verdana','Courier','Impact','Haettenschweiler'], textvariable=ftype, height=5)
Fontcombo.current(newindex=0)
Fontcombo.bind('<<ComboboxSelected>>', fontType)
Fontcombo.pack(side='right', padx=5)

frame2 = tk.Frame(root)
fileText = tk.Text(frame2, height=50, font=(ftype.get(),fsize.get()), undo='True',maxundo=10, selectbackground='#aaa', padx=10, pady=10)
fileText.bind("<Control-s>", saveFile)
fileText.bind("<Control-S>", saveFile)
fileText.pack(side='top',fill='both')
frame2.pack(fill='both')

root.mainloop()
