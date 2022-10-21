#threading and GUI:

# https://stackoverflow.com/questions/8309902/are-python-instance-variables-thread-safe
# You can use Locks, RLocks, Semaphores, Conditions, Events and Queues.
# And this article helped me a lot.
# http://www.laurentluce.com/posts/python-threads-synchronization-locks-rlocks-semaphores-conditions-events-and-queues/












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



