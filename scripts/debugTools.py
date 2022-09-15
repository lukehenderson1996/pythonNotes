#tools to make debugging faster & easier 
#Version 2.0
import ctypes
import numpy
# #TO BE IMPLEMENTED:
# import inspect
# import pprint

def info(label, obj, format='normal', treeLevel=0, dictKey=''):
    """Prints info about an object\n
    Args:
        label [str]: the label name of the object to be analyzed\n
        obj [any]: the object to be analyzed\n
        format [str, optional]: 
            normal: [recursive, if necessary] step thru obj\n
            dir: print external and internal dir() results
    Notes:
        usage example: dt.info('myObj', myObj)"""
    
    prefix = '\t'*treeLevel

    #ctypes array
    if isinstance(obj, ctypes.Array):
        prStr = '\tContents: [ '
        for element in obj:
            prStr += hex(element) + ' '
        print(prStr + ']')

    #normal python types:
    if format=='normal':
        if treeLevel==0:
            preText = prefix + f'{label} is '
        else:
            preText = prefix
        if obj is None:
            print(preText + 'None' + f'\t\t{type(obj)}')
        elif not ( isinstance(obj, dict) or isinstance(obj, list) or isinstance(obj, tuple) ):  #not hasattr(obj, '__iter__'):
            #Obj not iterable
            print(preText + dictKey + f'{obj}\t\t{type(obj)}')
        else:
            #Obj is iterable
            print(preText + 'iterable, of ' + f'type {type(obj)}, contents:')
            if len(obj)==0:
                print(prefix + '\tEmpty, length of zero')
            else:
                for el in obj:
                    if isinstance(obj, dict):
                        info(type(obj[el]), obj[el], treeLevel=treeLevel+1, dictKey= el+': ')
                    else:
                        info(type(el), el, treeLevel=treeLevel+1)
    elif format=='dir':
        dirList = dir(obj)
        internalDirList = []
        externalDirList = []
        for el in dirList:
            if el[0:2]=='__':
                internalDirList.append(el)
            else:
                externalDirList.append(el)
        print('\n' + f'Internal dir() of {label}: ')
        print(internalDirList)
        print('\n' + f'External dir() of {label}: ')
        print(externalDirList)

        print('\n\n' + f'Stepping through external dir() of {label}:')
        for el in externalDirList:
            #replicate object.internalElement()
            objElement = getattr(obj, el)
            info(el, objElement, format='normal', treeLevel=1)
    elif format=='test':
        pass
    #test out pprint and inspect modules here