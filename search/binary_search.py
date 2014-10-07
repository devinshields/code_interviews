#!/usr/bin/env python
'''
https://en.wikipedia.org/wiki/Binary_search_algorithm

be aware of recursive vs. iterative vs. deferred detection of equality
'''


def binary_search(arr, x, imin=0, imax=None):
  ''' assumes arr is sorted, finds the index of x in arr if it exists.
      returns -1 of it doesn't. Ignores duplicates and boundry conditions. '''
  if not imax:
    imax = len(arr)

  # key not found
  if (imax < imin):
    return -1

  imid = imin + (imax - imin)/2
  mid_key = arr[imid]

  if x < mid_key:
    return binary_search(arr, x, imin, imid-1)
  elif x > mid_key:
    return binary_search(arr, x, imid+1, imax)
  elif mid_key == x:
    return imid



def binary_search_iterative(A, key, imin=0, imax=None):
  if not imax:
    imax = len(A)
  while imax >= imin:
      imid = imin + (imax-imin)/2
      if A[imid] == key:
        return imid
      elif A[imid] < key:
        imin = imid + 1
      else:
        imax = imid - 1
  return -1




def test():

  # test data and preliminary sort
  test_string = 'In computer science, a binary search or half-interval search algorithm finds the position of a specified input value (the search "key") within an array sorted by key value'.replace(' ', '')
  keys_sorted = ''.join(sorted(test_string))

  # run the search - recursive
  indx = binary_search(keys_sorted, 'I')

  assert 'I' == keys_sorted[indx]
  assert indx == keys_sorted.index('I')
  assert binary_search(keys_sorted, 'q') == -1


  # run the iterative version
  indx = binary_search_iterative(keys_sorted, 'I')

  assert 'I' == keys_sorted[indx]
  assert indx == keys_sorted.index('I')
  assert binary_search_iterative(keys_sorted, 'q') == -1

  
  print test_string
  print keys_sorted

  pass

if __name__ == '__main__':
  test()

