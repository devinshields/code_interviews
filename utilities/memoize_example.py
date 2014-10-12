#!/usr/bin/env python
'''    '''

def memoize(f):
    ''' a simple memoization decorator '''
    cache = {}
    def memf(*x):
        if x not in cache:
            cache[x] = f(*x)
        return cache[x]
    return memf



@memoize
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)



def test():

    print fib(100)

if __name__ == '__main__':
    test()

