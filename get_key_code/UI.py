#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Text, BOTH, DISABLED, NORMAL, END

APPNAME = "WRITER TEST"
WELCOME_MSG = "Welcome to {}\n".format(APPNAME)

class Output(Text):
  
    def __init__(self, parent):
        Text.__init__(self, parent)   
        
        self.parent = parent
        self.initUI()
        
    def initUI(self):
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        self.parent.title("{}".format(APPNAME))
        self.parent.geometry('{}x{}'.format(sw,sh))
        self.parent.bind('<KeyPress>', self.onKeyPress)
        self.pack(fill=BOTH, expand=1)
        self.config(background='black', foreground='white', font=('Courier', 12))
        self.insert('end', '{}\n'.format(WELCOME_MSG))
        self.config(state=DISABLED)
    
    def onKeyPress(self, event):
        self.config(state=NORMAL)
        self.delete(1.0, END)
        self.insert('end', 'You pressed: {}'.format(event.keycode))
        self.config(state=DISABLED)

class UI():
    
    def __init__(self):
        self.root = Tk()
        self.app = Output(self.root)
        self.root.mainloop()

ui = UI()