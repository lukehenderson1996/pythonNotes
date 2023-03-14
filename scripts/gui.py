"""Thread-safe GUI module. Follows a producer-consumer structure utilizing a queue"""

# Author: Luke Henderson
__version__ = '2.42'

import os
import time
from datetime import datetime
# import contextlib
import tkinter as tk
from threading import Thread
import queue

import colors as cl
import debugTools as dt

DEFAULT_UPDATE_DELAY = 100/1000 #(seconds)
MAX_Q_SIZE = 50
Q_MAXED_WARN_DELAY = 5 #(seconds)

class LABEL:
    """Helper class for creation of custom labels"""
    idNum = 0

    # id : str
    # labelText : str #str or list of str
    color : str
    size : int
    font : str
    x : int
    y : int

    def __init__(self, color='Black', size=12, font="Helvetica", labType='text'):
        """generate unique LABEL object. Not thread safe\n
        Args:
            id [int]: unique ID for new custom label. Recommend making this
                the same as the variable name in main code
        Notes:
            labType (label type):
                text
                textInd
                    use this to create a number or string indicator with label on top.\n
                    cannot change location after creation
        Usage (outdated):
            'myLabel', "~Label's Text~", 'Blue', 18
        """
        #handle id, not thread safe due to simultaneous calls racing incrementation
        #print(f'ID: {id(self)}') #could also use this for thread safe version
        self.id= LABEL.idNum
        LABEL.idNum += 1
        #optional args
        self.color = color
        self.size = size
        self.font = font
        self.labType = labType
        #internal instance vars to be set in a second step
        self.labelText = ''
        self.x = 380
        self.y = 30
        #special labType
        if self.labType == 'textInd':
            self.indLabel = None
            
    def set(self, labelText, x=None, y=None, **kwargs):
        '''\n
        Args:
            labelText [str, int, float]: text to display\n
            x [int, optional]: default 380\n
            y [int, optional]: default 30
        Optional kwargs:
            indLabel [str, int, float]: label of text indicator'''
        #regular text label
        if not labelText is None:
            self.labelText = str(labelText)
        if not x is None:
            self.x = x
        if not y is None:
            self.y = y
        if self.labType == 'textInd':
                #text indicator, could be numeric or str
                #error handling
                if not (('indLabel' in kwargs) or (not self.indLabel is None)):
                    cl.red(f'GUI LABEL Error: set expected parameter "indLabel"')
                    return
                #set vars
                if self.indLabel is None:
                    #setting for the first time, need indLabel
                    self.indLabel = str(kwargs['indLabel'])
                    self.y= int(self.y - self.size*2)
        return self

class GUI:
    """Outer layer to drive App class in a separate thread"""

    def __init__(self, guiQ, windowTitle='Python GUI', updateDelay=None, quiet=False):
        """Initialize the gui\n
        Args:
            guiQ [queue.queue object]: queue of tasks to be consumed/executed
                Note: This is the only way to interact with a presently
                    running gui.
                Usage:
                    str, int, or float will be printed to aPrint\n
                    list: forms a custom command object.
                        Note: only supports length of 2 for the time being\n
                        list[0] [str]: The function to be called, such as aPrint\n
                        list[1] [any]: passed as argument to called function
                        example: guiQ.put(['aPrint', 'Hello, world!'])
            windowTitle [str, optional]: the object to be analyzed\n
            updateDelay [float, seconds, optional]: timing to update with
            quiet [bool, optional]: controls whether gui/app classes will print to CMD
        Notes:
            Can set these variables after init:
                windowGeom [str, currently not in use]: size/location of gui window. format:
                    format: XxY+(-)Xoff+(-)Yoff
                    example: '766x792+-7+0'"""
        self.guiQ = guiQ
        self.windowTitle = windowTitle
        self.updateDelay = updateDelay
        self.quiet = quiet
        #extra customization to be set after init
        self.windowGeom = '768x792+-8+0' #'766x792+-7+0' #currently not in use

    def start(self):
        """Starts gui in separate thread, non blocking"""
        mainThd = Thread(target=self.mainLoop, daemon=True)
        mainThd.start()

    def mainLoop(self):
        """blocking init and mainloop, to be threaded"""
        #init app
        self.root = tk.Tk()
        self.app=App(self.guiQ, self.updateDelay, self.quiet, self.root)
        #set init args
        self.root.wm_title(self.windowTitle)
        self.root.geometry(self.windowGeom) #to prevent eye sore of extra window movement
        self.root.state('zoomed')

        #start mainloop
        self.app.startGUI = True
        self.root.mainloop()

class App(tk.Frame):
    def __init__(self, quiQ, updateDelay, quiet, master=None):
        # self.root
        tk.Frame.__init__(self, master)
        # tk.Frame.wm_title('windowTitle')
        # tk.Frame.geometry('766x792+-7+0') #"900x500+0+0") #XxY+(-)Xoff+(-)Yoff
        #queue management vars
        self.guiQ = quiQ
        self.lastQWarning = 0 #beginning of time.time()
        #misc vars
        self.updateDelay = updateDelay
        self.quiet = quiet
        self.master = master 
        
        #init default labels
        self.rollPrHt = 11 #11
        self.label2 = tk.Label(text="", fg="Black", font=("Consolas", self.rollPrHt), justify='left')
        self.label2.place(x=0,y=0)
        self.label = tk.Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=500,y=5)

        # create button, link it to clickExitButton()
        self.exitButton = tk.Button(text="Quit", command=self.clickExitButton)
        self.exitButton.place(x=670, y=5)

        #init internal variables
        self.startGUI = False
        if self.updateDelay is None: 
            self.updateDelay = DEFAULT_UPDATE_DELAY
        self.rollPList = []
        self.kill = False
        self.killClearance = False
        self.userLabels = {}
        self.firstRun = True

        #start main outer loop
        if not self.quiet:
            cl.blue('Successful start ' + cl.CMDCYAN + 'GUI thread')
        self.outerLoop()

    """---------------------------------------GUI main "outer" loop---------------------------------------"""
    def outerLoop(self):
        while not self.startGUI:
            self.after(int(self.updateDelay*1000), self.outerLoop)
            return
        if self.firstRun:
            self.firstRun = False
            self.outerLoopInit()
        if self.kill == True:
            self.killGUI()
            return

        #update ongoing activities
        self.update_clock()

        #-------------------------------------------consume queue-------------------------------------------
        #convert multithreaded queue to single threaded, single loop task list
        task = []
        #self.aPrint('\t' + 'Checking Queue:')
        qsize = self.guiQ.qsize() #approximate q size (not reliable)
        if qsize > 0:
            #warn if too long
            if qsize > MAX_Q_SIZE:
                if time.time()-self.lastQWarning > Q_MAXED_WARN_DELAY:
                    self.printBoth(f'GUI Warning: Queue too long, of length {qsize}')
                    self.lastQWarning = time.time()
            #process queue
            doneCollecting = False
            while not doneCollecting:
                try:
                    task.append(self.guiQ.get(block=False))
                    self.guiQ.task_done()
                except queue.Empty:
                    doneCollecting = True
                if len(task) >= MAX_Q_SIZE:
                    doneCollecting = True
            # with contextlib.suppress(queue.Empty):
            #     task = self.guiQ.get(block=False)
            #     self.guiQ.task_done()

        #process task
        while len(task) > 0:
            taskItem = task.pop(0)
            if isinstance(taskItem, list):
                #list
                if len(taskItem) == 2:
                    #list of correct length (valid command structure)
                    if hasattr(self, taskItem[0]):
                        selfFnc = getattr(self, taskItem[0])
                        selfFnc(taskItem[1])
                    else:
                        self.aPrint(f'GUI Error: List object contains invalid command "{taskItem[0]}"')
                else:
                    self.aPrint(f'GUI Error: List object is of invalid length {len(taskItem)}')
            elif isinstance(taskItem, str):
                #string
                self.aPrint(taskItem)
            elif isinstance(taskItem, int) or isinstance(taskItem, float):
                #int or float
                self.aPrint(str(taskItem))
            elif isinstance(taskItem, LABEL):
                #custom LABEL object
                self.setLabel(taskItem)
            else:
                #object of another data type
                self.aPrint('GUI Error: Invalid datatype given')

        #loop back (Note the .after method is non-blocking)
        self.after(int(self.updateDelay*1000), self.outerLoop)

    """-----------------------utilities-----------------------"""
    def outerLoopInit(self):
        #dynamic window geometry adjustment for left half of screen
        maxWd = int(self.master.winfo_width())
        self.wWd = int(maxWd/2)
        self.wHt = int(self.master.winfo_height()-9)
        self.wX = int(self.master.winfo_rootx()-8)
        self.wY = int(self.master.winfo_rooty()-23)
        # print(f'Current geom: {self.master.winfo_geometry()}')
        # print(f'Fixed:        {self.wWd}x{self.wHt}+{self.wX}+{self.wY}')
        self.master.state('normal')
        self.master.wm_geometry(f'{self.wWd}x{self.wHt}+{self.wX}+{self.wY}')

    def killGUI(self):
        # while not self.killClearance:
        #     pass
        if not self.quiet:
            cl.blue('Exiting ' + cl.CMDCYAN + 'GUI thread')
        self.quit()
        # exit()

    def clickExitButton(self):
        self.kill = True

    """-------------------assorted functions------------------"""
    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        self.label.configure(text=now)

    def aPrint(self, pText):
        """rolling printer "app Print" similar to cmd/shell print()
        pText = text to print, can include newlines"""
        BUFFER_SIZE = int((self.wHt-44)/self.rollPrHt*1.30/2 - 1) #43
        if not isinstance(pText, str):
            cl.red('GUI Error: aPrint() List contains something other than a string')
            return
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
            """Prints to cmd/shell and app rolling printer"""
            print(pText)
            self.aPrint(pText)

    def printError(self, pText):
            """Prints red to cmd/shell and black to app rolling printer"""
            cl.red(pText)
            self.aPrint(pText)

    def setLabel(self, lb):
        """Creates/updates custom labels\n
        Create: utilizes all input object parameters\n 
        Update: updates text, position, color of label\n
        Args:
            lb [obj of class LABEL]: input parameter object. (short for label)\n
        Vars from this class' __init__():
            self.userLabels = {}"""
        if lb.id in self.userLabels:
            self.userLabels[lb.id].configure(text=lb.labelText, fg=lb.color, font=(lb.font, lb.size))
        else:
            self.userLabels[lb.id] = tk.Label(text=lb.labelText, fg=lb.color, font=(lb.font, lb.size))
        self.userLabels[lb.id].place(x=lb.x,y=lb.y)

        if lb.labType == 'textInd':
            id2 = lb.id + 0.1
            if id2 in self.userLabels:
                pass #self.userLabels[id2].configure(text=lb.labelText, fg=lb.color, font=(lb.font, lb.size))
            else:
                self.userLabels[lb.id].configure(borderwidth=2, relief="sunken")
                self.userLabels[id2] = tk.Label(text=lb.indLabel, fg=lb.color, font=(lb.font, lb.size))
                self.userLabels[id2].place(x=lb.x, y=int(lb.y-lb.size*2) )
        
