"""Test code for gui.py"""

# Author: Luke Henderson 

import os
import time
from datetime import datetime
import queue

import colors as cl
import debugTools as dt
import gui

cl.green('Program Start')
progStart = time.time()

guiQ = queue.Queue()
dw = gui.GUI(guiQ, updateDelay=None, quiet=False)
myVar = dw.start()

time.sleep(2)
guiQ.put(['printBoth', 'should be printed in both places...'])
guiQ.put(['printBoth', 'filler...'])
time.sleep(2)
guiQ.put(['newLabel', "~Label's Text~", 'Blue', 18])
time.sleep(2)
os.system('pause')

# time.sleep(2)
# guiQ.put('Message from beyond')
# time.sleep(2)
# guiQ.put(1)
# time.sleep(2)
# guiQ.put(3.1415926)
# time.sleep(2)
# guiQ.put(['aPrint', 'Custom command success'])
# time.sleep(2)
# guiQ.put(['aPrint', str(9.87654)])
# os.system('pause')