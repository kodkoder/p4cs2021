# Messing with lists
#
# Author: Tomasz
#  The program outputs all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. 

import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for n in range(0,numberOfNumbers):
    queue.append(random.randint(0,rangeTo))

print("queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print("current Number is {} and the queue is {} ".format(currentNumber, queue))

print ("The queue is now empty...")