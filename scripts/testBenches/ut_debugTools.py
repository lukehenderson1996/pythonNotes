'''Unit test for debugTools.py (validated for v)'''

# Author: Luke Henderson
__version__ = '0.1'
_PY_VERSION = (3, 11)

import time
import unittest
from unittest.mock import patch
from io import StringIO
import sys

import debugTools as dt 

progStart = time.time()

class TestDtModule(unittest.TestCase):
    @patch('builtins.print')
    def test_info(self, mock_print):
        prIter = 0

        dt.info('simpleObj', 'stringcontents')
        self.assertEqual(len(mock_print.call_args_list), prIter := prIter+2)
        first_call_args = mock_print.call_args_list[-2]
        second_call_args = mock_print.call_args_list[-1]
        self.assertEqual(first_call_args, unittest.mock.call("stringcontents is simpleObj\t\t<class 'str'>"))
        self.assertEqual(second_call_args, unittest.mock.call("\x1b[0m", end='', flush=True))

        dt.info('myObj', None)
        self.assertEqual(len(mock_print.call_args_list), prIter := prIter+2)
        first_call_args = mock_print.call_args_list[-2]
        second_call_args = mock_print.call_args_list[-1]
        self.assertEqual(first_call_args, unittest.mock.call("None is myObj\t\t<class 'str'>"))
        self.assertEqual(second_call_args, unittest.mock.call("\x1b[0m", end='', flush=True))

if __name__ == '__main__':
    import colors as cl
    cl.gn("Unit Test Start")
    unittest.main()