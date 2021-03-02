# This is code will find some text in an access file
#
# Author: Tomasz

import re

regex = "\[.*\]"
filename = "smallerAccess.log"

with open(filename) as inputFile:
    for line in inputFile:
        foundTextList = re.findall(regex, line)
        if (len(foundTextList)!=0):      
            # print(foundTextfile)
            foundText = foundTextList[0]
            print(foundText)
            #print(foundText)
            # if I did not want the [] at the beginning and end
            # print(foundText[1:-1])
