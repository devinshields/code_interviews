#!/usr/bin/env python
'''
notes:  https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
        https://en.wikipedia.org/wiki/Quicksort#Optimizations
'''


def quicksort_recursive(arr):
  '''  http://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python  '''
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
 


def quicksort_recursive_list_comprehension(arr):
  ''' http://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Quicksort '''
  if arr == []:
    return []
  else:
    return quicksort_recursive_list_comprehension([x for x in arr[1:] if x< arr[0]]) + \
           arr[0:1] + \
           quicksort_recursive_list_comprehension([x for x in arr[1:] if x>=arr[0]])



def test():
  ''' unit tests for the various quicksorts '''

  # test data
  a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
  a0, a1 = tuple(a), tuple(sorted(a))

  #
  assert tuple(quicksort_recursive(a)) == a1

  assert tuple(quicksort_recursive_list_comprehension(a)) == a1


  #
  import __main__
  print '\n*** Tests Pass ***\tfor file: {0}\n'.format(__main__.__file__)


if __name__ == '__main__':
    test()

