#test code

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import logger as lg

cl.green('Program Start')
progStart = time.time()

import tkinter as tk
import gui

#init (dw = ??? widget?)
dw = gui.GUI("Miner Supervisor", 150)
dw.runMain()
