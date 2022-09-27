"""Thread-safe GUI module. Follows a producer-consumer structure utilizing a queue"""

# Author: Luke Henderson

import os
import time
from datetime import datetime
import contextlib
import tkinter as tk
from threading import Thread
import queue

import colors as cl
import debugTools as dt

GUI_MODULE_DEFAULT_UPDATE_DELAY = 100/1000

class GUI:
    """Outer layer to drive App class in a separate thread"""

    def __init__(self, guiQ, windowTitle='Python GUI', updateDelay=None, quiet=False):
        """Initialize the gui\n
        Args:
            guiQ [queue.queue object]: queue of tasks to be consumed/executed
                Note: This is the only way to interact with a presently\n
                running gui.
            windowTitle [str, optional]: the object to be analyzed\n
            updateDelay [float, optional]: timing to update with in seconds
            quiet [bool, optional]: controls whether gui/app classes will print to CMD
        Notes:
            Can set these variables after init:
                windowGeom: size/location of gui window. format:
                    format: XxY+(-)Xoff+(-)Yoff
                    example: '766x792+-7+0'"""
        self.guiQ = guiQ
        self.windowTitle = windowTitle
        self.updateDelay = updateDelay
        self.quiet = quiet
        #extra customization to be set after init
        self.windowGeom = '766x792+-7+0'

    def start(self):
        mainThd = Thread(target=self.mainLoop, daemon=True)
        mainThd.start()

    def mainLoop(self):
        #init app
        self.root = tk.Tk()
        self.app=App(self.updateDelay, self.quiet, self.root)
        #set init args
        self.app.guiQ = self.guiQ
        # self.app.updateDelay = self.updateDelay
        self.root.wm_title(self.windowTitle)
        self.root.geometry(self.windowGeom) 

        #start mainloop
        self.root.mainloop()

class App(tk.Frame):
    def __init__(self, updateDelay, quiet, master=None):
        # self.root
        tk.Frame.__init__(self, master)
        # tk.Frame.wm_title('windowTitle')
        # tk.Frame.geometry('766x792+-7+0') #"900x500+0+0") #XxY+(-)Xoff+(-)Yoff
        self.updateDelay = updateDelay
        self.quiet = quiet
        self.master = master

        #init default labels
        self.label2 = tk.Label(text="", fg="Black", font=("Consolas", 11), justify='left')
        self.label2.place(x=0,y=0)
        self.label = tk.Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=380,y=5)

        # create button, link it to clickExitButton()
        self.exitButton = tk.Button(text="Quit", command=self.clickExitButton)
        self.exitButton.place(x=550, y=0)

        #init internal variables
        if self.updateDelay is None: 
            self.updateDelay = GUI_MODULE_DEFAULT_UPDATE_DELAY
        self.rollPList = []
        self.x = 1
        self.kill = False
        self.killClearance = False

        #start main outer loop
        if not self.quiet:
            cl.blue('Successful start ' + cl.CMDCYAN + 'GUI thread')
        
        # while True:
        #     self.aPrint('If queue exists:')
        #     if hasattr(self, 'guiQ'):
        #         self.aPrint('\t' + "It's here!")
        #         with contextlib.suppress(queue.Empty):
        #             self.aPrint(self.guiQ.get(block=False))
        #     time.sleep(.01)

        self.outerLoop()

    '''---------------------------------------GUI main "outer" loop---------------------------------------'''
    def outerLoop(self):
        #bug is that there must be something else called "main loop" that gets started later, outer loop is already running before gui even goes up
        if self.kill == True:
            self.killGUI()
        self.update_clock()

        # #example print loop
        
        # self.aPrint(str(self.x) + ' Hello, world')
        # self.x += 1
        # self.aPrint(str(self.x))
        # self.x += 1

        #loop back
        self.after(int(self.updateDelay*1000), self.outerLoop)

    '''-----------------------utilities-----------------------'''
    def killGUI(self):
        # cl.yellow('gui.py attempting to kill thread(s)')
        # while not self.killClearance:
        #     pass
        
        # self.master.destroy() # THROWS CRAZY BUGS
        if not self.quiet:
            cl.blue('Exiting ' + cl.CMDCYAN + 'GUI thread')
        exit()

    def clickExitButton(self):
        self.kill = True

    '''-------------------assorted functions------------------'''
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.label.configure(text=now)

    def aPrint(self, pText):
        '''rolling printer "app Print" similar to cmd/shell print()
        pText = text to print, can include newlines'''
        BUFFER_SIZE = 42
        # BUFFER_SIZE_GUESS = 792/11*1.33*1.25 #not sure how this can be done
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

    def printBoth(self, pText):
            '''Prints to cmd/shell and app rolling printer'''
            print(pText)
            self.aPrint(pText)

