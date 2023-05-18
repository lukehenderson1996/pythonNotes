"""Test code for gui.py"""

# Author: Luke Henderson 

import os
import time
from datetime import datetime
import queue

import colors as cl
import debugTools as dt
import gui
import utils as ut

COMMON_FONTS = ['Trebuchet MS', #fonts present in both Windows and Ubuntu 22 (after microsoft fonts installed)
        'Webdings',
        'Arial Black',
        'Verdana',
        'Times New Roman',
        'Comic Sans MS',
        'Georgia',
        'Arial',
        'Courier New',
        'Impact']

cl.green('Program Start')
progStart = time.time()

guiQ = queue.Queue()
dw = gui.GUI(guiQ, updateDelay=0.001, quiet=True, windowMax=True) 
dw.start()

# #BRING FOCUS BACK TO CMD WINDOW (from chatGPT)
# import win32gui
# #Find the window handle of the cmd window (from chatGPT)
# hwnd = win32gui.GetForegroundWindow()
# #start GUI
# dw.start()
# # Bring the cmd window to the front and set the focus (from chatGPT)
# time.sleep(.1)
# win32gui.SetForegroundWindow(hwnd)

# #test fonts:
# import tkinter.font as tkf
# fontTuple = tkf.families()
# dt.info(fontTuple, 'fontTuple')
# #display fonts:
# fontsToIterate = COMMON_FONTS #fontTuple or COMMON_FONTS
# #big displays
# labelList = []
# for i, font in enumerate(fontsToIterate):
#     labelList.append(gui.LABEL(color='Black', size=24, font=font))
#     labelList[-1].set("fgijlpqtuvxy 00:1234  " + font, x=20, y=120+70*i)
#     guiQ.put(labelList[-1])
# #small displays
# labelList = []
# for i, font in enumerate(fontsToIterate):
#     labelList.append(gui.LABEL(color='Black', size=11, font=font))
#     labelList[-1].set("fgijlpqtuvxy 00:1234  " + font, x=1200, y=120+70*i)
#     guiQ.put(labelList[-1])
# #pause
# ut.pause()



# #simple tests
# guiQ.put('Message from beyond')
# guiQ.put(1)
# guiQ.put(3.1415926)
# guiQ.put(['aPrint', 'Custom command aPrint success'])
# guiQ.put(['printBoth', 'should be printed in both places...'])
# time.sleep(1)
# ut.pause()


# #rolling printer test
# guiQ.put('1-----------------------------------------------')
# for i in range(2, 100+1):
#     guiQ.put(i)
#     # time.sleep(.1)
# ut.pause()


# #maxed out queue test
# #set updateDelay to 1
# guiQ.put('1-----------------------------------------------')
# for i in range(2, 100+1):
#     guiQ.put(i)
#     # time.sleep(.1)
# ut.pause()


# #custom label tests
# #first label
# myLabel = gui.LABEL(color='Blue', size=26, font="Arial")
# myLabel.set("~Label's Text~", x=300, y=50)
# guiQ.put(myLabel)
# #second label
# labelTwo = gui.LABEL(color='Green', size=45, font="Arial")
# labelTwo.set("Hello, world", x=300, y=350)
# guiQ.put(labelTwo)
# #same label tests
# time.sleep(1)
# guiQ.put(labelTwo.set("changed text"))
# time.sleep(1)
# labelTwo.color = 'Purple'
# guiQ.put(labelTwo.set('Moved, purple', x=350, y=400))
# time.sleep(1)
# labelTwo.font = 'Courier New'
# labelTwo.size = 11
# guiQ.put(labelTwo.set('Courier New and 11'))
# time.sleep(1)
# labelTwo.size = 11
# guiQ.put(labelTwo.set('Font should stay at 11'))
# time.sleep(1)
# labelTwo.size = 11
# guiQ.put(labelTwo.set('Font should stay at 11'))
# time.sleep(1)
# labelTwo.size = 13
# guiQ.put(labelTwo.set('Font should increase to 13'))
# time.sleep(1)
# labelTwo.size = 26
# guiQ.put(labelTwo.set('Font should increase to 26'))
# time.sleep(1)
# labelTwo.size = 31
# guiQ.put(labelTwo.set('Font should increase to 31'))
# time.sleep(1)
# labelTwo.size = 14
# guiQ.put(labelTwo.set('Font should decrease to 14'))
# ut.pause()


# #test output templates:
# # l1 = Label(root, text="This", borderwidth=2, relief="groove")
# myLabel = gui.LABEL(labType='textInd', size=12)
# myLabel.set(0, x=300, y=300, indLabel="Indicator's Name")
# guiQ.put(myLabel)
# for i in range(1, 3):
#     time.sleep(1)
#     guiQ.put(myLabel.set(i))
# ut.pause()






#various labels
myLabel = gui.LABEL(color='Blue', size=12, font="Arial")
myLabel.set("Size 12 @ 300x300", x=300, y=300)
guiQ.put(myLabel)
myLabel2 = gui.LABEL(color='Blue', size=18, font="Arial")
myLabel2.set("Size 18 @ 400x400", x=400, y=400)
guiQ.put(myLabel2)
myLabel3 = gui.LABEL(color='Blue', size=26, font="Arial")
myLabel3.set("Size 26 @ 470x500", x=470, y=500)
guiQ.put(myLabel3)
myLabel4 = gui.LABEL(color='Blue', size=90, font="Arial")
myLabel4.set("Size 90 @ 600x600", x=600, y=600)
guiQ.put(myLabel4)

#fill up rolling printer
for i in range(45+1):
    prStr = str((str(i)+' ')*200)[:90]
    if i%2:
        prStr = '012345678 10---15---20---25---30---35---40---45---50---55---60---65---70---75---80---85---'
    guiQ.put(prStr)

#grid output
xRange = 2500 #oversize
yRange = 1500 #oversize
xlabelRes = 50 #40 #labels will overlap if too small
ylabelRes = 20
fontSize = 8
for yPos in range(50, yRange, 200):
    xGrid = []
    for xLoc in range(0, xRange, xlabelRes):
        xGrid.append(gui.LABEL(size=fontSize, color='green'))
        xGrid[-1].set(xLoc, x=xLoc, y=yPos)
        guiQ.put(xGrid[-1])
        time.sleep(.07)
for xPos in range(50, xRange, 200):
    yGrid = []
    for yLoc in range(0, yRange, ylabelRes):
        yGrid.append(gui.LABEL(size=fontSize, color='purple'))
        yGrid[-1].set(yLoc, x=xPos, y=yLoc)
        guiQ.put(yGrid[-1])
        time.sleep(.07)

ut.pause()
