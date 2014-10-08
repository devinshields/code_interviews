#!/usr/bin/env python
'''

https://docs.python.org/2/library/collections.html#collections.deque

collections.deque

  Deques are a generalization of stacks and queues (the name is pronounced "deck"
  and is short for "double-ended queue"). Deques support thread-safe, memory efficient
  appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

'''

import collections


def test():

  dqueue = collections.deque()

  for i in range(10):
    dqueue.append(i)

  while dqueue:
    print dqueue.pop()
    print dqueue.popleft()



if __name__ == '__main__':
    test()

