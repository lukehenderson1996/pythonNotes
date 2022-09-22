"""tutorial.py teaches some simple python examples
Uncomment one block at a time"""

# Author: Luke Henderson 

import os
import time

import colors as cl
import debugTools as dt
import logger as lg

#constants go here:
SPREADSHEET_HEADER = ['Hour','BTC','ETH']

#main code goes here:



# #pieces of data literally typed out in text are called "literals"
# 6 #int
# 3.4 #float
# 'string'
# "string, no difference"
# [] #empty list
# [3, 4, 7.7] #list of int/float
# ['list', 'of', 'strings']
# #you can also have nested things
# ['list', 'with a ', 'list', [1, 2, 3]]
# #you can save these to a variable and inspect them with debugTools
# #using dt.info
# emptyList = []
# myFloat = 3.4
# complicated = ['list', 'with a ', 'list', [1, 2, 3]]
# print('Inspecting emptyList')
# dt.info('emptyList', emptyList)
# print('Inspecting myFloat')
# dt.info('myFloat', myFloat)
# print('Inspecting complicated')
# dt.info('complicated', complicated)




# #additionally, everything in python is an object
# #you can view the directory of an object with dt.dirInfo()
# #cl.[SOME COLOR] prints in a color
# cl.blue('Printing dirInfo for the number 6:')
# dt.dirInfo('number', 6)
# cl.blue('Printing dirInfo for a string:')
# dt.dirInfo('string', 'some text')

# #to use the first method on the list:
# cl.blue('Printing first attribute of string: ')
# myString = 'some text'
# print(myString.capitalize())
# print(myString.upper())

# #Lastly, how to use the logger to make a simple spreadsheet 
# #of crypto prices per hour
# #SPREADSHEET_HEADER = ['Hour','BTC','ETH'] #this was a constant at the start of the file anyway
# cl.blue(f'logging using columns: {SPREADSHEET_HEADER}')
# cryptoLog = lg.LOGGER(logCols=SPREADSHEET_HEADER)
# cryptoLog.simpLog(['3', 18000, 1500])
# cryptoLog.simpLog(['4', 19000, 1450])
# cryptoLog.simpLog(['5', 20000, 1400])
