'''Test code for logger.py (validated for v)'''

# Author: Luke Henderson
__version__ = '1.0'
_PY_VERSION = (3, 7)

import os
import time
from datetime import datetime

import colors as cl
import debugTools as dt
import logger as lg

cl.green('Program Start')
progStart = time.time()

# #simple logging case
# sLog = lg.LOGGER(logCols=['Try Number', 'Profitability'])
# sLog.simpLog([1, 1.05])

# #multiple logs case
# myLog = lg.LOGGER(logCols=['Time', 'BTCUSD', 'Site'], csv=True, xml=True)
# btcPrice = 20
# for i in range(4):
#     time.sleep(.01)
#     currTime = time.time()
#     btcPrice += 1
#     print(f'writing btc {btcPrice} for time {currTime}')
#     myLog.simpLog([currTime, btcPrice, 'example.com'])
# myLog.close()

# #test ResultData class
# resultData = 18000
# unit = 'USD/BTC'
# site = 'coingecko.com'
# capTime = time.time()
# cgData = lg.ResultData(resultData=resultData, unit=unit, site=site, capTime=capTime)
# cgData.resultData[0] = 18500
# dt.info('cgData', cgData)

# #test prefix, subfolder, etc functionality of logger
# prefix = input('Enter subfolder/datalog prefix: ')
# myLog = lg.LOGGER(logCols=['Time','Site'], prefix=prefix, quiet=False, csv=True, xml=True)
# myNamedLog = lg.LOGGER(logCols=['Date','Time','Site'], filename='custom name', prefix=prefix, quiet=False)
# debugLog = lg.LOGGER(None, prefix='debug\VERBOSE', quiet=False, xml=True)
# #need further debug on subfolder usage
# #for this example, it neglects to put VERBOSE in subfolder/debug, just tries datalogs/debug
# #also will not check for existence of subfolder and create
# #also needs to check for existence of datalogs folder and create if necessary

'''test filepath handling for platform'''

# #rel path
# sLog = lg.LOGGER(logCols=['Try Number', 'Profitability'], quiet=False)
# sLog.simpLog([1, 1.05])

#incorrect rel path
sLog = lg.LOGGER(logCols=['Try Number', 'Profitability'], prefix='my\\folders/to/use', quiet=False)
sLog.simpLog([1, 1.05])

# #absolute path
# sLog = lg.LOGGER(logCols=['Try Number', 'Profitability'], 
#                  absPath='/home/luke/Documents/projects/pythonNotes/datalogs/missingFolder/sub3/hello.csv', quiet=False)
# sLog.simpLog([1, 1.05])

# #incorrect abs path
# sLog = lg.LOGGER(logCols=['Try Number', 'Profitability'], 
#                  absPath='/home/luke/Documents/projects/pythonNotes\\datalogs\\missingFolder\\sub3\\hello.csv', quiet=False)
# sLog.simpLog([1, 1.05])
