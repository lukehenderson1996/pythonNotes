'''Test code for colors.py (validated for v1.0)'''

# Author: Luke Henderson
__version__ = '1.0'
_PY_VERSION = (3, 11)

import time

import colors as cl

cl.gn('Test Bench Start')
progStart = time.time()

cl.bl('blue')
cl.rd('red')
cl.gn('green')
cl.yl('yellow')
cl.pr('purple')
cl.gy('gray')
cl.cy('cyan')

print(f'{cl.BL}custom {cl.GY}colors {cl.PR}per {cl.GN}word{cl.EC}')
print('back to normal')

print(f'{cl.UL}underlined{cl.EC} word')