"""Miscellaneous assorted utilities"""

# Author: Luke Henderson
# Version 1.22

import sys
import os
import platform
import time
from datetime import datetime

import colors as cl
import debugTools as dt

class printProgress:
    """Simple percent of progress printout, non blocking"""

    def __init__(self, len, dispQty):
        """Progress update of significant percent updates\n
        Args:
            len [int]: total length of loop to give progress updates on\n
            dispQty [int]: quantization of updates, example 5 -> every 5%
        Notes:
            0% 25% 50% 75% 100% Done!
        Usage:
            pb = ut.printProgress(len(lenSpot), 5)\n
            pb.update(inIdx)\n
            print('Done!')"""
        self.len = len
        self.dispQty = dispQty
        self.lastPercent = 0
        print(f'0% ', end='', flush=True)

    def update(self, currIdx):
        '''Call to determine if update should be printed/print\n
        Args:
            currIdx [int]: Current index of progress, to be incremented up towards self.len'''
        percent = round(currIdx/self.len*100)
        if percent >= self.lastPercent+self.dispQty:
            print(f'{percent}% ', end='', flush=True)
            self.lastPercent += self.dispQty

class ProgressBar:
    """Progress bar, non blocking"""
    
    def __init__(self, len, dispLen):
        """Progress bar of significant percent updates
            Uses sys.stdout, may overwrite print()'s from other portions of program
        Args:
            len [int]: total length of loop to give progress updates on\n
            dispLen [int]: total length (characters) of progress bar output
        Notes:
            [####################..............................]
            [##################################################]"""
        self.len = len
        self.dispLen = dispLen
        self.lastPercent = 0

    def update(self, currIdx):
        '''Call to determine if update should be printed/print\n
        Args:
            currIdx [int]: Current index of progress, to be incremented up towards self.len'''
        done = round(self.dispLen * currIdx / self.len)
        if self.dispLen-done == 1:
            sys.stdout.write("\r[%s]" % ('#' * (self.dispLen)) )  
        else:
            sys.stdout.write("\r[%s%s]" % ('#' * done, '.' * (self.dispLen-done)) )    
        sys.stdout.flush()

def pause():
    '''Like os.system('pause') in Windows but with a newline'''
    input('Press any key to continue . . .\n')

def printBoolTable(inDict):
    """Prints out contents/info of a large ammount of boolean values
        in a short format with 1's and 0's
    Args:
        inDict [dict]: must contain lists of bools, example:
            {'key1':[],'key2':[]...} (string keys only)"""
    for key in inDict:
        boolStr = ''
        for el in inDict[key]:
            if el:
                boolStr += cl.CMDCYAN + str(int(el))
            else:
                boolStr += cl.HEADER + str(int(el))
        print(key + ': [ ' + boolStr + cl.ENDC + f' ] len={len(inDict[key])}')

def dateStr(day) -> str:
    '''Converts day of month or month number int into two digit str\n
    Args:
        day [int]: day of the month (or month number)
    Return:
        [str]: day w/ leading zero ('00' to '31'), (or to '12') '''
    if day < 10:
        return '0' + str(day)
    else:
        return str(day)

def humTime():
    '''Returns current time and date in human readable format\n
    Return:
        [tuple]: humReadDate [str], humReadTime [str]
    Usage: 
        humReadDate, humReadTime = ut.humTime()'''
    dateObj = datetime.now()
    humReadDate = dateObj.strftime("20%y-%m-%d")
    humReadTime = dateObj.strftime("%H:%M:%S.%f")[:-3]
    return humReadDate, humReadTime

def humTimeAndObj():
    '''Returns current time and date in human readable format\n
    \t and a matching datetime.now() object
    Return:
        [tuple]: humReadDate [str], humReadTime [str], dateObj [datetime.now()]
    Usage:
        humReadDate, humReadTime, dateObj = ut.humTimeAndObj()'''
    dateObj = datetime.now()
    humReadDate = dateObj.strftime("20%y-%m-%d")
    humReadTime = dateObj.strftime("%H:%M:%S.%f")[:-3]
    return humReadDate, humReadTime, dateObj

def humTimeList():
    '''Returns a list of current time and date strings in human readable format\n
    Return:
        [list]: [humReadDate [str], humReadTime [str]]'''
    humReadDate, humReadTime = humTime()
    return [humReadDate, humReadTime]

def countFileLines(path):
    '''Fast way to count total lines in a file\n
    Args:
        path [str]: path to file
    Return:
        [int] total number of lines'''
    with open(path, 'rb') as f:
        c_generator = countGenerator(f.raw.read)
        count = sum(buffer.count(b'\n') for buffer in c_generator)
        print(f'Total lines for file: {count + 1}')
    return count + 1

def countGenerator(reader):
    '''Counter subfunction for countFileLines()\n
    Args:
        reader [?]: ?? - f.raw.read
    Notes:
        Unknown functionality, need more research'''
    b = reader(1024 * 1024)
    while b:
        yield b
        b = reader(1024 * 1024)

def flRnd(num, decPlace=None):
    '''Converts to float and rounds\n
    Args:
        num [any number type]: number to be converted/rounded\n
        decPlace [int, optional]: ammount of decimal places to be rounded to
            default: whole number
            0: whole number, 1: tenths place, -1: tens place
    Return:
        [float] converted/rounded number'''
    return round(float(num), decPlace)

def winCurrHandle():
    '''Find the window handle of the cmd window\n
    Return:
        hwnd [Windows window handle]: handle of current window'''
    if platform.system() == "Windows":
        import win32gui

        windowsList = []
        def callback(handle, _):
            if win32gui.IsWindowVisible(handle):
                windowTitle = win32gui.GetWindowText(handle)
                if windowTitle:
                    windowClass = win32gui.GetClassName(handle)
                    windowsList.append((windowTitle, windowClass))
            return True
        win32gui.EnumWindows(callback, None)
        
        filename = os.path.basename(sys.argv[0])

        #get window name
        className = None
        windowName = None
        AlreadyFound = False
        for item in windowsList:
            if 'niceHash' in item[0] and 'ConsoleWindowClass' in item[1]:
                if AlreadyFound:
                    cl.red(f'Error (utils.py): Multiple window hanldes found for file "{filename}"')
                    exit()
                else:
                    AlreadyFound = True
                    className = item[1]
                    windowName = item[0]
        if windowName is None or className is None:
            cl.red(f'Error (utils.py): Window hanlde not found for file "{filename}"')
            exit()

        hwnd = win32gui.FindWindow(className, windowName)
        # hwnd = win32gui.GetForegroundWindow()
        return hwnd
    else:
        return None

def winFocus(hwnd):
    '''Focus on given window\n
    Args:
        hwnd [Windows window handle]: handle to bring into focus
    Usage:
        hwnd = ut.winCurrHandle()\n
        #start gui\n
        ut.winFocus(hwnd)'''
    if platform.system() == "Windows":
        import win32gui
        time.sleep(.1)
        win32gui.SetForegroundWindow(hwnd)
    else:
        cl.yellow("This machine is not running Windows, will skip focus utility")