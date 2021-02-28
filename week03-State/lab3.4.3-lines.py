# lines.py
#
# Author: Tomasz
# The program creates array that has tuples of x,y coordinates. It prints out the distance each of those points are from the origin.
# The Distance for a point to origin is dist. = sqrt( X2 + Y2)

import math

points = [(1,2),(3,3),(4,3)]
for x, y in points:
    dist = math.sqrt(x**2 + y**2)

    print('point({},{}) is {:.2f} , from the origin'.format(x,y,dist))
