'''Name/Purpose/Description'''

# Author: xxxxx
__version__ = '0.1'
_PY_VERSION = (3, 11)

'external imports here'

'internal imports here'

class NAME: #or, ClassName
    '''NAME class'''
    internalConstant = 2e-6

    def __init__(self, arg1, arg2, optionalArg3='normal'):
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
        #internal automatically called init code here
        self.internalVariable = 'variable content'
        pass

    def init(self):
        '''non-automatic init'''
        pass

    def _internalFunction(self, arg1):
        pass

    def publicFunction(self, arg1, arg2) -> float:
        return 2.3
    

if __name__ == '__main__':
    'test code start message here'
    'test bench here'