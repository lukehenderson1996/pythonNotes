'''Name/Purpose/Description'''

# Author: Luke Henderson 
__version__ = '0.1'
_PY_VERSION = (3, 0)

import time
import os

import colors as cl
import debugTools as dt

cl.gn('Program Start')
progStart = time.time()

#----------------------------------------------------------------init----------------------------------------------------------------
#assert correct module versions 
modV = {cl:   '1.0',
        dt:   '3.22',}
for module in modV:
    errMsg = f'Expecting version {modV[module]} of "{os.path.basename(module.__file__)}". Imported {module.__version__}'
    assert module.__version__ == modV[module], errMsg

#-------------------------------------------------------------main loop--------------------------------------------------------------

