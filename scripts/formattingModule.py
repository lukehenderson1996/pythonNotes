"""Short description"""

# Author: xxxxx

'external imports here'

'internal imports here'

class NAME: #or, ClassName
    """Short description"""
    internalConstant = 2e-6

    def __init__(self, arg1, arg2, optionalArg3='normal'):
        """Short description\n
        Args:
            arg1 [str]: the label name of the object to be analyzed\n
            arg2 [float]: the object to be analyzed\n
            optionalArg3 [str, optional]: 
                'normal' (default, recursive if necessary) step thru obj\n
                    and print relevant info
                'dir' print external and internal dir() results
        Return:
            [int] 0 for pass
        Notes:
            notes here"""
        #internal automatically called init code here
        self.internalVariable = 'variable content'
        pass

    def init(self) -> None:
        """non-automatic init"""
        pass

    def _internalFunction(self, arg1) -> None:
        pass

    def publicFunction(self, arg1, arg2) -> None:
        pass