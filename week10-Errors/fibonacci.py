import logging
logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    a = 0
    b = 1
    fibonacciSequence = [0]
    # we have one in the list already so number - 1 times
    # this is not the most efficient code
    # could have used yield
    for i in range(1,number):
        if number == 0:
            return []
        fibonacciSequence.append(b)
        if number < 0:
            raise ValueError('number must be > 0')
        # this is funky code make a = b and b = a + b
        a , b = b, a + b
        logging.debug("%d: %s",number, fibonacciSequence)


if __name__ == '__main__':
    # tests will go here
    print("all good")

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'
