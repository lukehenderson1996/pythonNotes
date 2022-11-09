"""Test code for debugTools.py"""

# Author: Luke Henderson 

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt

cl.green('Program Start')
progStart = time.time()

class myClass():
    def __init__(self, argumentOne, argumentTwo):
        self.initedElement = 'StartsWithThis'
        self.passedArg1 = argumentOne
        self.passedArg2 = argumentTwo

#string
cl.blue('Testing a simple string with color')
dt.info('simpleObj', 'stringcontents', format='normal', color='WARNING')
print('\n\n')

#various simple tests
cl.blue('Testing None')
myObj = None
dt.info('myObj', myObj, format='normal')
cl.blue('Testing Tuple')
myObj = ('hey', 'hi', 'hello')
dt.info('myObj', myObj, format='normal')
cl.blue('Testing List')
myObj = ['hey', 'hi', 'hello']
dt.info('myObj', myObj, format='normal')
cl.blue('Testing List of int')
internalObj = [1, 3]
dt.info('myObj', internalObj, format='normal')
cl.blue('Testing List of assorted things')
myObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
dt.info('myObj', myObj, format='normal')
print('\n\n')

#dictionary of many things
cl.blue('Testing a dictionary of assorted things')
internalObj = [1, 3, {'dictItem1': 'stringCont', 'dictItem2': 829.44}, 'last item of internalObj']
midObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
myObj = {'name': 'Dionysia', 'age': 28, 'bigInternal': midObj, 'location': 'Athens'}
dt.info('myObj', myObj, format='normal')

#class
cl.blue('Testing a class')
classInst = myClass('passedOneCont', 'passedTwoCont')
dt.dirInfo('classInst', classInst)

#pprint
cl.blue('pprint:')
dt.pprintInfo(myObj)

#dictionary bug test, for version 2.6
#should be able to support str/int/float/bool keys
dt.info('trickyDict', {'name': 'Dionysia', 0: 'This one has an int key', 5.345: 'This one has a float key', True: 'This one has a bool key'})

#getting entire scope of currently running python script:
cl.blue('Global variables:')
dt.info('globals', dict(globals()))
cl.blue('Local variables:')
dt.info('locals', dict(locals()))