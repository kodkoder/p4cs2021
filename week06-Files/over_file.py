# Messing with overwriting
#
# Author: tomasz

filename = 'count.txt'
def writeNumber(number):
    with open(filename,'wt') as f:
        # write takes a string so we need to convert
        f.write(str(number))

# test it
writeNumber(1000032223)