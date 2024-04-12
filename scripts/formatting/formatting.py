'''Short description'''

# Author: xxxxx 
__version__ = '0.0'
_PY_VERSION = (3, 11)

'external imports here'

'internal imports here'

'program start message here'

#----------------------------------------------------------------init----------------------------------------------------------------
#assert correct module versions 
modV = {'modObj':   '1.0',
        'modObj':   '3.22'}
for module in modV:
    errMsg = f'Expecting version {modV[module]} of "{os.path.basename(module.__file__)}". Imported {module.__version__}'
    assert module.__version__ == modV[module], errMsg

CONSTANT_NAME = "constant's content"

def internal_functions_here(arg1, arg2, optionalArg3='normal'):
    '''Short description\n
    Args:
        arg1 [str]: short description\n
        arg2 [float]: short description\n
        optionalArg3 [str, optional]: description
            typical input:
                long description
            typical input: short description
    Return:
        [int] 0 for pass
    Notes:
        notes here'''
    pass
    return 0

#-------------------------------------------------------------main loop--------------------------------------------------------------

multiLineImplicit  = print('1 ' + '2 ' + 
                           '3 ' + '4')

multiLineExplicit = '1' + \
                    '2' + \
                    '3' + \
                    '4'
