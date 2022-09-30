'''Module to make debugging faster & easier'''

# Author: Luke Henderson 
# Version 2.6

import colors as cl
import ctypes
import numpy
import pprint

def info(label, obj, format='normal', treeLevel=0, dictKey='', color='normal'):
    """Prints info about an object\n
    Args:
        label [str]: the label name of the object to be analyzed\n
        obj [any]: the object to be analyzed\n
        format [str, optional]: 
            currently not in use
        treeLevel [int, internal]: can use for tabbing, used internally
            for recursive tabbing
        dictKey [str, internal]: used internally for printing out dictionary
            keys
        color [str, optional]:
            uses colors.py constants to change printer color\n
            example: use 'OKBLUE' for colors.OKBLUE

    Notes:
        usage example: dt.info('myObj', myObj)
            assumed using "import debugTools as dt"
        advanced usage example:
            dt.info('myObj', myObj, format='dir', color='OKBLUE')
        internal arguments are optional and normally just used for recursion"""
    prefix = '\t'*treeLevel + dictKey
    if not color=='normal':
        prefix = getattr(cl, color) + prefix

    #ctypes array
    if isinstance(obj, ctypes.Array):
        prStr = '\t' + 'Contents: [ '
        for element in obj:
            prStr += hex(element) + ' '
        print(prStr + ']')
        return

    #normal python types:
    #setup prefix/pretext
    if treeLevel==0:
        preText = prefix + f'{label} is '
    else:
        preText = prefix
    #analyze
    if obj is None:
        #obj is None
        print(preText + 'None' + '\t\t' + f'{type(obj)}')
    elif not ( isinstance(obj, dict) or isinstance(obj, list) or isinstance(obj, tuple) ):  #not hasattr(obj, '__iter__'):
        #obj not iterable, print contents and type
        print(preText + f'{obj}\t\t{type(obj)}')
    else:
        #obj is iterable, and of type dict, list, or tuple
        print(preText + f'iterable, of type {type(obj)}, length {len(obj)}, contents:')
        if len(obj)==0:
            #empty iterable
            print(prefix + '\t' + 'Empty, length of zero')
        else:
            #valid iterable, iterate and print info
            for el in obj:
                if isinstance(obj, dict):
                    info(type(obj[el]), obj[el], treeLevel=treeLevel+1, dictKey= str(el)+': ')
                else:
                    info(type(el), el, treeLevel=treeLevel+1)
    

    #ENDC to fix printing back to normal
    print(cl.ENDC, end='', flush=True)

def dirInfo(label, obj, format='normal', treeLevel=0, color='normal'):
    """Prints and analyzes dir() info about an object\n
    Args:
        label [str]: the label name of the object to be analyzed\n
        obj [any]: the object to be analyzed\n
        format [str]: 'normal', or 'ext' for ext step through only\n
        treeLevel [int, internal]: can use for tabbing, used internally
            for recursive tabbing
        color [str, optional]:
            uses colors.py constants to change printer color\n
            example: use 'OKBLUE' for colors.OKBLUE"""
    prefix = '\t'*treeLevel
    if not color=='normal':
        prefix = getattr(cl, color) + prefix

    dirList = dir(obj)
    internalDirList = []
    externalDirList = []
    for el in dirList:
        if el[0:2]=='__':
            internalDirList.append(el)
        else:
            externalDirList.append(el)
    if format=='normal':
        print('\n' + f'Internal dir() of {label}: ')
        print(internalDirList)
        print('\n' + f'External dir() of {label}: ')
        print(externalDirList)
        print('\n')

    print(f'Stepping through external dir() of {label}:')
    for el in externalDirList:
        #replicate object.internalElement()
        objElement = getattr(obj, el)
        info(el, objElement, format='normal', treeLevel=1, dictKey=el+': ')
    
    #ENDC to fix printing back to normal
    print(cl.ENDC, end='', flush=True)

def pprintInfo(obj):
    '''Wrapper for pprint'''
    pprint.pprint(obj)
