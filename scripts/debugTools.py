'''Module to make debugging faster & easier'''

# Author: Luke Henderson 
# Version 2.9

import sys

import colors as cl

def info(label, obj, treeLevel=0, dictKey='', color='normal'):
    """Prints info about an object\n
    Args:
        label [str]: the label name of the object to be analyzed\n
        obj [any]: the object to be analyzed\n
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
            dt.info('myObj', myObj, color='OKBLUE')
        internal arguments are optional and normally just used for recursion
        supported libraries:
            numpy, pprint, requests, ctypes"""
    prefix = '\t'*treeLevel + dictKey
    if not color=='normal':
        prefix = getattr(cl, color) + prefix

    #ctypes array
    if 'ctypes' in sys.modules:
        import ctypes
        if isinstance(obj, ctypes.Array):
            prStr = '\t' + 'Contents: [ '
            for element in obj:
                prStr += hex(element) + ' '
            print(prStr + ']')
            return

    #numpy array numpy.ndarray
    if 'numpy' in sys.modules:
        import numpy
        if isinstance(obj, numpy.ndarray):
            print(f'Numpy array "{label}", length {len(obj)}')
            if len(obj) < 10:
                for el in obj:
                    print('\t' + str(el))
            else:
                for i in [0, 1]:
                    print('\t' + str(obj[i]))
                print('\t...\t...\t...\t...\t...')
                for i in [-2, -3]:
                    print('\t' + str(obj[i]))
            return

    #requests api response
    if 'requests' in sys.modules:
        import requests
        if isinstance(obj, requests.models.Response):
            print(f'Requests api response "{label}", status code: {obj.status_code}, reason: {obj.reason}')
            info('url', obj.url)
            info('elapsed', obj.elapsed)
            info('headers', dict(obj.headers))
            info('json', obj.json())
            return
        # #requests json
        # if isinstance(obj, requests.models.Response.json):
        #     print('Functionality for requests.models.Response.json not complete')
        #     return

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
        info(el, objElement, treeLevel=1, dictKey=el+': ')
    
    #ENDC to fix printing back to normal
    print(cl.ENDC, end='', flush=True)

def pprintInfo(obj):
    '''Wrapper for pprint\n
    Args:
        obj [any]: object to pprint'''
    if 'pprint' in sys.modules:
        import pprint
        pprint.pprint(obj)
    else:
        cl.red('Error, pprint not installed')
