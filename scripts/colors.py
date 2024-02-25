'''Module for easy colored text on terminal prints'''

# Author: Luke Henderson
__version__ = '1.0'
_PY_VERSION = (3, 11)

import os
import platform

if platform.system() == 'Windows':
    os.system('') #enable VT100 escape sequence for Windows 10

ENDC = '\033[0m' #ENDC, resets to normal
UNDERLINE = '\033[4m'

BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
PURPLE = '\033[95m'
GRAY = '\033[90m'
CYAN = '\033[96m'

EC = ENDC
UL = UNDERLINE

BL = BLUE
RD = RED
GN = GREEN
YL = YELLOW
PR = PURPLE
GY = GRAY
CY = CYAN

'''Prints in color of function name
Args:
    printStr [str, other]: input text to print in color
        converted via str()
Notes:
    Each function has a shorthand version that takes up the same ammount of space as a print()
    Example:
        print() or
        cl.bl()'''
def ul(printStr):
    '''Prints in UNDERLINE'''
    print(UNDERLINE + str(printStr) + ENDC)
def underline(printStr):
    ul(printStr)
    
def bl(printStr):
    '''Prints in BLUE'''
    print(BLUE + str(printStr) + ENDC)
def blue(printStr):
    bl(printStr)
    
def rd(printStr):
    '''Prints in RED'''
    print(RED + str(printStr) + ENDC)
def red(printStr):
    rd(printStr)
    
def gn(printStr):
    '''Prints in GREEN'''
    print(GREEN + str(printStr) + ENDC)
def green(printStr):
    gn(printStr)
    
def yl(printStr):
    '''Prints in YELLOW'''
    print(YELLOW + str(printStr) + ENDC)
def yellow(printStr):
    yl(printStr)
    
def pr(printStr):
    '''Prints in PURPLE'''
    print(PURPLE + str(printStr) + ENDC)
def purple(printStr):
    pr(printStr)
    
def gy(printStr):
    '''Prints in GRAY'''
    print(GRAY + str(printStr) + ENDC)
def gray(printStr):
    gy(printStr)
    
def cy(printStr):
    '''Prints in CYAN'''
    print(CYAN + str(printStr) + ENDC)
def cyan(printStr):
    cy(printStr)
    




