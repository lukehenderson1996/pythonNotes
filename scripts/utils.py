"""Miscellaneous assorted utilities"""

# Author: Luke Henderson
# Version 1.0

import sys

import colors as cl

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
    '''Like os.system('pause') but with a newline'''
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

def dateStr(day):
    '''Converts day of month int into two digit str\n
    Args:
        day [int]: day of the month
    Return:
        [str]: day w/ leading zero ('00' to '31') '''
    if day < 10:
        return '0' + str(day)
    else:
        return str(day)

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
