"""Test code for gui.py"""

# Author: Luke Henderson 

import os
import time
from datetime import datetime
import queue

import colors as cl
import debugTools as dt
import gui
import utils

cl.green('Program Start')
progStart = time.time()

guiQ = queue.Queue()
dw = gui.GUI(guiQ, updateDelay=0.05, quiet=True) 
dw.start()

# #simple tests
# guiQ.put('Message from beyond')
# guiQ.put(1)
# guiQ.put(3.1415926)
# guiQ.put(['aPrint', 'Custom command aPrint success'])
# guiQ.put(['printBoth', 'should be printed in both places...'])
# time.sleep(1)
# utils.pause()


# #rolling printer test
# guiQ.put('1-----------------------------------------------')
# for i in range(2, 100+1):
#     guiQ.put(i)
#     # time.sleep(.1)
# utils.pause()


# #maxed out queue test
# #set updateDelay to 1
# guiQ.put('1-----------------------------------------------')
# for i in range(2, 100+1):
#     guiQ.put(i)
#     # time.sleep(.1)
# utils.pause()


# #custom label tests
# #first label
# myLabel = gui.LABEL(color='Blue', size=26, font="Helvetica")
# myLabel.set("~Label's Text~", x=300, y=50)
# guiQ.put(myLabel)
# #second label
# labelTwo = gui.LABEL(color='Green', size=45, font="Helvetica")
# labelTwo.set("Hello, world", x=300, y=350)
# guiQ.put(labelTwo)
# #same label tests
# time.sleep(1)
# guiQ.put(labelTwo.set("changed text"))
# time.sleep(1)
# labelTwo.color = 'Purple'
# guiQ.put(labelTwo.set('Moved, purple', x=350, y=400))
# time.sleep(1)
# labelTwo.font = 'consolas'
# labelTwo.size = 11
# guiQ.put(labelTwo.set('Consolas and 11'))
# utils.pause()


#test output templates:
# l1 = Label(root, text="This", borderwidth=2, relief="groove")
myLabel = gui.LABEL(labType='textInd', size=12)
myLabel.set(0, x=300, y=300, indLabel="Indicator's Name")
guiQ.put(myLabel)
for i in range(1, 3):
    time.sleep(1)
    guiQ.put(myLabel.set(i))
utils.pause()


# #grid output
# for yPos in range(50, 1000, 200):
#     xGrid = []
#     for xLoc in range(0, 1000, 100):
#         xGrid.append(gui.LABEL(size=12))
#         xGrid[-1].set(xLoc, x=xLoc, y=yPos)
#         guiQ.put(xGrid[-1])
#     time.sleep(0.1)
# for xPos in range(50, 1000, 200):
#     yGrid = []
#     for yLoc in range(0, 1000, 100):
#         yGrid.append(gui.LABEL(size=12))
#         yGrid[-1].set(yLoc, x=xPos, y=yLoc)
#         guiQ.put(yGrid[-1])
#     time.sleep(0.1)
# utils.pause()
