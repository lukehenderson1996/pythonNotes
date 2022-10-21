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


#rolling printer test
guiQ.put('1-----------------------------------------------')
for i in range(2, 100+1):
    guiQ.put(i)
    # time.sleep(.1)
utils.pause()


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

