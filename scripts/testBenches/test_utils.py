'''Test code for utils.py (validated for v1.5)'''

# Author: Luke Henderson
__version__ = '1.1'
_PY_VERSION = (3, 11)

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import utils as ut

cl.green('Program Start')
progStart = time.time()

#progress printout
loopLength = 100
pb = ut.printProgress(loopLength, 25)
for i in range(loopLength):
    time.sleep(0.02)
    pb.update(i)
print('Done!')

#progress bar
loopLength = 100
pb = ut.ProgressBar(loopLength, 75)
for i in range(loopLength):
    time.sleep(0.02)
    pb.update(i)
print()

#pause
ut.pause()

#bool table
table = {'key1':[True, True, False, False], 
    'key2':[False, True, True, False], 
    'key3':[False, False, True, True] }
ut.printBoolTable(table)

#float round
print(ut.flRnd(14.678))
print(ut.flRnd(14.678, -1))

#test filepath handler
myPth = ut.pth('')
print(myPth)
#absolute
baseDir = os.path.dirname(os.getcwd())
myPth = ut.pth(baseDir + f'\\datalogs\\using\\absolute')
print(myPth)
#relative
myPth = ut.pth('/datalogs/using/relative', 'rel1')
print(myPth)

#test list/dict functions
myDictList = [{'key1':'value1', 'key2':None}, {'key1':'value2', 'key2':None}, {'key1':'value3', 'key2':None}]
cl.blue('Original:')
dt.pprintInfo(myDictList)
cl.blue('Converted to dict:')
dt.pprintInfo(myListDict := ut.listConv(myDictList))
cl.blue('Converted to list:')
dt.pprintInfo(myDictList := ut.dictConv(myListDict))