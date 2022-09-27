"""Short description"""

# Author: xxxxx 

'external imports here'

'internal imports here'

#init here

CONSTANT_NAME = "constant's content"

def internal_functions_here(arg1, arg2, optionalArg3='normal') -> int:
    """Short description\n
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
        notes here"""
    pass
    return 0



#main code here
multiLineImplicit  = print(
    '1 ' + '2 ' + 
    '3 ' + '4')

multiLineExplicit = '1'   \
    + '2' \
    + '3' \
    + '4'
