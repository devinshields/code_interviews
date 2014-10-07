#!/usr/bin/env python
'''
Knuth shuffle
  linear time

https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle

'''

import random


def shuffle(arr):
  for i in range(len(arr)-1, 1, -1):
    j = random.randrange(i+1)
    swap = arr[j]
    arr[j] = arr[i]
    arr[i] = swap
  return arr



def test():

  alphabet = tuple(chr(i) for i in range(ord('a'), ord('a')+26))
  scramble = tuple(shuffle(list(alphabet)))

  print alphabet
  print scramble

  pass

if __name__ == '__main__':
  test()

