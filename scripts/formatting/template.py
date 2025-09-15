'''Name/Purpose/Description'''

# Author: Luke Henderson 
__version__ = '0.1'
_PY_VERSION = (3, 0)

import time
import os

import colors as cl
import debugTools as dt
import utils as ut

cl.gn('Program Start')
progStart = time.time()

#----------------------------------------------------------------init----------------------------------------------------------------
#assert correct module versions
ut.checkModV({cl:   '1.0',
              dt:   '3.22',})

#-------------------------------------------------------------main loop--------------------------------------------------------------

