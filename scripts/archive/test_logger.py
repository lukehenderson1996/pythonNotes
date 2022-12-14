"""Test code for logger.py"""

# Author: Luke Henderson 

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

# #test prefix, subfolder, etc functionality of logger
# prefix = input('Enter subfolder/datalog prefix: ')
# myLog = lg.LOGGER(logCols=['Time','Site'], prefix=prefix, quiet=False, csv=True, xml=True)
# myNamedLog = lg.LOGGER(logCols=['Date','Time','Site'], filename='custom name', prefix=prefix, quiet=False)
# debugLog = lg.LOGGER(None, prefix='debug\VERBOSE', quiet=False, xml=True)