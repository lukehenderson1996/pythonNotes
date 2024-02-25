'''Test code for debugTools.py (validated for v3.22)'''

# Author: Luke Henderson
__version__ = '2.1'
_PY_VERSION = (3, 11)

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import utils as ut

PRINT_EN = True
if PRINT_EN:
    cl.gn('Test Code Start')
progStart = time.time()

class myClass():
    def __init__(self, argumentOne, argumentTwo):
        self.initedElement = 'StartsWithThis'
        self.passedArg1 = argumentOne
        self.passedArg2 = argumentTwo

#string
cl.bl('Testing a simple string with color')
dt.info('stringcontents', 'simpleObj')
dt.info('stringcontents', 'simpleObj', color='YL')
print('\n\n')

#various simple tests
cl.bl('Testing None')
myObj = None
dt.info(myObj, 'myObj')
cl.bl('Testing Tuple')
myObj = ('hey', 'hi', 'hello')
dt.info(myObj, 'myObj')
cl.bl('Testing List')
myObj = ['hey', 'hi', 'hello']
dt.info(myObj, 'myObj')
cl.bl('Testing List of int')
internalObj = [1, 3]
dt.info(internalObj, 'myObj')
cl.bl('Testing List of assorted things')
myObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
dt.info(myObj, 'myObj')
print('\n\n')

#dictionary of many things
cl.bl('Testing a dictionary of assorted things')
internalObj = [1, 3, {'dictItem1': 'stringCont', 'dictItem2': 829.44}, 'last item of internalObj']
midObj = ['hey', internalObj, 'hello', None, [], (None, None, [], None)]
myObj = {'name': 'Dionysia', 'age': 28, 'bigInternal': midObj, 'location': 'Athens'}
dt.info(myObj, 'myObj')

#class
cl.bl('Testing a class')
classInst = myClass('passedOneCont', 'passedTwoCont')
dt.dirInfo('classInst', classInst)

#pprint
cl.bl('pprint:')
dt.pprintInfo(myObj)

#dictionary bug test, for version 2.6
#should be able to support str/int/float/bool keys
trickyDict = {'name': 'Dionysia', 0: 'This one has an int key', 5.345: 'This one has a float key', True: 'This one has a bool key'}
dt.info(trickyDict, 'trickyDict')

#getting entire scope of currently running python script:
cl.bl('Global variables:')
dt.info(dict(globals()), 'globals')
cl.bl('Local variables:')
dt.info(dict(locals()), 'locals')

#generate pythonic literal
print('\n\n')
cl.bl('Pythonic literal of classInst')
dt.genPyLiteral(trickyDict, 'trickyDict')
print('')
dt.genPyLiteral(myObj, 'myObj')
print('\n')
#the actual text it produced:
trickyDict = {"name": "Dionysia", 0: "This one has an int key", 5.345: "This one has a float key", True: "This one has a bool key"}

myObj = {"name": "Dionysia", "age": 28, "bigInternal": ["hey",
        [1, 3, {"dictItem1": "stringCont", "dictItem2": 829.44}, "last item of internalObj"],
        "hello",
        None,
        [],
        (None, None, [], None)], "location": "Athens"}


#get size info
dt.sizeInfo(myObj, 'myObj', color='YL')

