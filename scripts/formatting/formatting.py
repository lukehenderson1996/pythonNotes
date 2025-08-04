'''Name/Purpose/Description'''

# Author: xxxxx 
__version__ = '0.1'
_PY_VERSION = (3, 11)

'external imports here'

'internal imports here'

'program start message here'

#----------------------------------------------------------------init----------------------------------------------------------------
#assert correct module versions 
modV = {'modObj':   '1.0',
        'modObj':   '3.22',}
for module in modV:
    errMsg = f'Expecting version {modV[module]} of "{os.path.basename(module.__file__)}". Imported {module.__version__}'
    assert module.__version__ == modV[module], errMsg

CONSTANT_NAME = "constant's content"

def internalFunctionsHere(arg1, arg2, optionalArg3='normal'):
    '''Short description
    Args:
        arg1 (str): short description
        arg2 (float): short description
        optionalArg3 (str, optional): description
            typical input: short description
            typical input:
                long description
    Returns:
        int: 0 for pass
    Examples:
        examples here
    ## Notes:
        notes here'''
    pass


#-------------------------------------------------------------main loop--------------------------------------------------------------

multiLineImplicit  = print('1 ' + '2 ' + 
                           '3 ' + '4')

multiLineExplicit = '1' + \
                    '2' + \
                    '3' + \
                    '4'
