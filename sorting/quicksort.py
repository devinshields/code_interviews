#!/usr/bin/env python
'''  '''

def quicksort_recursive(arr):
  '''
  from:  http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
  note:  https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
         https://en.wikipedia.org/wiki/Quicksort#Optimizations
  '''
  # initialize temp variables
  less, pivotList, more = [], [], []
  
  # base case, empty array can be sorted
  if len(arr) <= 1:
    return arr
  else:
    # otherwise recurse
    pivot = arr[0]
    for i in arr:
      if i < pivot:
        less.append(i)
      elif i > pivot:
        more.append(i)
      else:
        pivotList.append(i)
    less = quicksort_recursive(less)
    more = quicksort_recursive(more)
    return less + pivotList + more
 

def test():
  ''' unit tests for the various quicksorts '''

  # test data
  a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
  a0, a1 = tuple(a), tuple(sorted(a))

  #
  assert tuple(quicksort_recursive(a)) == a1


  import __main__
  print '\n*** Tests Pass ***\tfor file: {0}\n'.format(__main__.__file__)


if __name__ == '__main__':
    test()

