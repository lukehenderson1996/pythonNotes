'''Test code to run all unit tests'''

# Author: Luke Henderson
__version__ = '0.1'
_PY_VERSION = (3, 11)

import time
import unittest

import colors as cl
import testBenches.ut_debugTools as ut_debugTools

cl.green('All Test Benches Start')
progStart = time.time()


loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(ut_debugTools))

runner = unittest.TextTestRunner(verbosity=2)
results = runner.run(suite)

# print('Total Tests Run:', results.testsRun)
# print('Failures:', len(results.failures))
# print('Errors:', len(results.errors))
# print('Skipped:', len(results.skipped))