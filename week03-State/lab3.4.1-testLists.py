# Messing with lists
# Author: andrew Beatty
# demonstrating that a list can have hetrogenious types

aList = [23,'hi', True]

# normal
for item in aList:
    print(item)

# prints out the list in reverse
print ('\n'.join(map(str,aList[::-1])))