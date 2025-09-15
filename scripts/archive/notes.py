'''Python notes'''

# Author: Luke Henderson
__version__ = '1.1'
_PY_VERSION = (3, 11)


fruits = ["loquat", "jujube", "pear", "watermelon", "apple"]
colors = ["brown", "orange", "green", "pink", "purple"]
for fruit, color in zip(fruits, colors):
    print(color, fruit)


#getting element AND int index in same for loop
for n, fruit in enumerate(fruits):
    print(n, fruit, sep=' -- ')
# #or:
# for index, el in enumerate(dirList, start=0)
#             print(el)
#             print(index)



