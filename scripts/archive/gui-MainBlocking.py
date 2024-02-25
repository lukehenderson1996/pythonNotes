'''Old gui code, block the main thread'''

# Author: Luke Henderson
__version__ = '1.0'
_PY_VERSION = (3, 7)

import os
import time
from datetime import datetime
import colors as cl
import debugTools as dt

import tkinter as tk
import contextlib


class GUI:
    """Outer layer to drive App class"""

    def __init__(self, windowTitle, updateDelay):
        """Initialize the gui"""
        self.root = tk.Tk()
        self.app=App(self.root)
        self.app.updateDelay = updateDelay
        self.root.wm_title(windowTitle)
        self.root.geometry('766x792+-7+0') #XxY+(-)Xoff+(-)Yoff

    def runMain(self):
        #start loop
        cl.blue('Successful start ' + cl.CYAN + 'GUI')
        self.root.mainloop()

class App(tk.Frame):
    def __init__(self, master=None):
        # self.root
        tk.Frame.__init__(self, master)
        # tk.Frame.wm_title('windowTitle')
        # tk.Frame.geometry('766x792+-7+0') #"900x500+0+0") #XxY+(-)Xoff+(-)Yoff
        self.master = master
        self.label2 = tk.Label(text="", fg="Black", font=("Consolas", 11), justify='left')
        self.label2.place(x=0,y=0)
        self.label = tk.Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=380,y=5)

        # create button, link it to clickExitButton()
        self.exitButton = tk.Button(text="Quit", command=self.clickExitButton)
        self.exitButton.place(x=550, y=0)

        self.updateDelay = 0 #default 0 second update delay
        self.rollPList = []
        self.x = 1
        self.kill = False
        self.killClearance = False
        #shell variables init
        self.shellKillReq = False
        self.shellFeed = []

        self.outerLoop()

    def outerLoop(self):
        if self.kill == True:
            self.killGUI()
        self.update_clock()
        # #example print loop
        # self.aPrint(str(self.x) + ' Hello, world')
        # self.x += 1
        # self.aPrint(str(self.x))
        # self.x += 1
        self.after(self.updateDelay, self.outerLoop)

    def killGUI(self):
        cl.yellow('Attempting to kill all threads')
        while not self.killClearance:
            pass
        exit()

    def clickExitButton(self):
        self.kill = True

    def update_clock(self):
        # now = time.strftime('%H:%M:%S')
        # print(root.geometry())
        now = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.label.configure(text=now)
        
    def printBoth(self, pText):
        '''Prints to cmd and app'''
        print(pText)
        self.aPrint(pText)

    def aPrint(self, pText):
        '''app Print
        pText = text to print'''
        BUFFER_SIZE = 42
        if not isinstance(pText, str):
            cl.red('Error: List contains something other than a string')
            exit()
        #split on newlines
        splitPText = pText.split('\n')
        #wrap text
        for el in splitPText:
            while len(el) > 94:
                self.rollPList.append(el[0:93])
                el = el[93:]
            self.rollPList.append(el)
        #remove old prints to make rolling command line style printer
        while len(self.rollPList) > BUFFER_SIZE:
            self.rollPList.pop(0)
        pStr = ''
        for el in self.rollPList:
            pStr += el + '\n'
        self.label2.configure(text=pStr)




        

# class Window(tk.Frame):
#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)
#         self.master = master
#         self.pack(fill=tk.BOTH, expand=1)

#         menu = tk.Menu(self.master)
#         self.master.config(menu=menu)

#         fileMenu = tk.Menu(menu)
#         fileMenu.add_command(label="Item")
#         fileMenu.add_command(label="Exit", command=self.exitProgram)
#         menu.add_cascade(label="File", menu=fileMenu)

#         editMenu = tk.Menu(menu)
#         editMenu.add_command(label="Undo")
#         editMenu.add_command(label="Redo")
#         menu.add_cascade(label="Edit", menu=editMenu)

#         text = tk.Label(self, text="HELLO WORLD")
#         text.place(x=70,y=90)
#         text.pack()

#     def exitProgram(self):
#         exit()
        
# root = tk.Tk()
# app = Window(root)
# root.wm_title("Tkinter window")
# root.geometry("32000x400000")
# root.mainloop()




# class Window(tk.Frame):

#     def __init__(self, master=None):
#         tk.Frame.__init__(self, master)        
#         self.master = master

#         # widget can take all window
#         self.pack(fill=tk.BOTH, expand=1)

#         # create button, link it to clickExitButton()
#         exitButton = tk.Button(self, text="Exit", command=self.clickExitButton)

#         # place button at (0,0)
#         exitButton.place(x=0, y=0)

#     def clickExitButton(self):
#         exit()
        
# root = tk.Tk()
# app = Window(root)
# root.wm_title("Tkinter button")
# root.geometry("320x200")
# root.mainloop()













#from Najeed :)
# myBackground = "#181818"
# primText = "#FFFFFF"

# def click():
#     print("you clicked")

# window = tk.Tk()
# window.geometry("420x420")
# window.title("Outputs")
# window.config(background=myBackground)

# button = tk.Button(window, text="click me", command=click)
# button.pack()


# dispText = tk.Canvas(window, textvariable = 'abcdefg')
# dispText.pack()

# window.mainloop() #place window

# os.system('pause')