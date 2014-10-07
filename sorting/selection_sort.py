#!/usr/bin/env python
'''  '''


def selection_sort(arr):
  for i in range(len(arr)):
    mindex = i
    for j in range(i, len(arr)):
      if arr[j] < arr[mindex]:
        mindex = j
    swap = arr[i]
    arr[i] = arr[mindex]
    arr[mindex] = swap
  return arr



def test():
  test_arr = list('hello, world')
  eval_arr = tuple(sorted(test_arr))

  assert eval_arr == tuple(selection_sort(test_arr))

  pass

if __name__ == '__main__':
  test()

