#make text look unique

import os
os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
CMDBLUE = '\033[36m'
CMDCYAN = '\033[96m'

# class colorPrinter:
#     """Custom print colors"""

#normal print colors
def blue(printStr):
    """prints in blue, expects a string input"""
    print(OKBLUE + printStr + ENDC)

def red(printStr):
    """prints in red, expects a string input"""
    print(FAIL + printStr + ENDC)

def green(printStr):
    """prints in green, expects a string input"""
    print(OKGREEN + printStr + ENDC)

def yellow(printStr):
    """prints in green, expects a string input"""
    print(WARNING + printStr + ENDC)

def purple(printStr):
    """prints in purple, expects a string input"""
    print(HEADER + printStr + ENDC)

#cmd colors (echo command):
def cmdBlue(printStr):
    """prints in blue, expects a string input, can accept %DATE/TIME% placeholders"""
    os.system('echo ' + CMDBLUE + printStr + ENDC)
    
def cmdCyan(printStr):
    """prints in cyan, expects a string input, can accept %DATE/TIME% placeholders"""
    os.system('echo ' + CMDCYAN + printStr + ENDC)

