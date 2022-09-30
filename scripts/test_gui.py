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
dw = gui.GUI(guiQ, updateDelay=2, quiet=False)
myVar = dw.start()

time.sleep(1)
guiQ.put('Message from beyond')
os.system('pause')