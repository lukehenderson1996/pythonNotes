#main.py written by Luke Henderson
#Miner Supervisor, controls when/how a cryptocurrency mining computer operates

import os
import time
from datetime import datetime
import tkinter as tk
from threading import Thread


import colors as cl
import debugTools as dt
import gui

cl.green('Program Start')
progStart = time.time()

class myClass():
    def __init__(self, argumentOne, argumentTwo):
        self.initedElement = 'StartsWithThis'
        self.passedArg1 = argumentOne
        self.passedArg2 = argumentTwo

# dt.info('simpleObj', 'stringcontents', format='normal')

# myObj = None
# myObj = ('hey', 'hi', 'hello')
# myObj = ['hey', 'hi', 'hello']
# internalObj = [1, 3]
# myObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
# print('\n\n')
# dt.info('myObj', myObj, format='normal')

# print('\n\n')
# internalObj = [1, 3, {'dictItem1': 'stringCont', 'dictItem2': 829.44}, 'last item of internalObj']
# midObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
# myObj = {'name': 'Dionysia', 'age': 28, 'bigInternal': midObj, 'location': 'Athens'}
# dt.info('myObj', myObj, format='normal')


#classes
# classInst = myClass('passedOneCont', 'passedTwoCont')
# dt.info('classInst', classInst, format='dir')


# #random stuff
# dt.info('Test', cl, format='dir')

