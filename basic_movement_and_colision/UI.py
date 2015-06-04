#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import Tk, Text, BOTH, DISABLED, NORMAL, END

APPNAME = "WRITER TEST"
WELCOME_MSG = "Welcome to {}\n".format(APPNAME)

class Output(Text):
  
    def __init__(self, parent,inhandler):
        Text.__init__(self, parent)   
        
        self.parent = parent
        self.inh = inhandler
        
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
        self.inh.pressed_key(event.keycode)

class UI():

    def __init__(self,inhandler,outhandler):
        self.outh = outhandler
        outhandler.add_listener(self)
        self.root = Tk()
        self.app = Output(self.root,inhandler)
        self.root.mainloop()
    
    def update(self):
        self.app.config(state=NORMAL)
        self.app.delete(1.0, END)
        self.app.insert('end', '{}'.format(self.outh.output))
        self.app.config(state=DISABLED)