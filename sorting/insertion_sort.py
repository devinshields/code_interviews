#!/usr/bin/env python
'''
note: really fast on mostly sorted arrays
'''


def insertion_sort(arr):
  for i in range(len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
      swap = arr[j-1]
      arr[j-1] = arr[j]
      arr[j] = swap
      j -= 1
  return arr



def test():
  test_arr = list('hello, world')
  eval_arr = tuple(sorted(test_arr))

  assert eval_arr == tuple(insertion_sort(test_arr))

  pass

if __name__ == '__main__':
  test()

