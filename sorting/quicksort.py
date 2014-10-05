#!/usr/bin/env python
'''
https://en.wikipedia.org/wiki/Quicksort#Choice_of_pivot
https://en.wikipedia.org/wiki/Quicksort#Optimizations
http://stackoverflow.com/questions/17773516/in-place-quicksort-in-python


  - in the fancy, O(1) space complexity version, the 
        
'''


import random


def sub_partition(array, start, end, idx_pivot):
    ''' returns the position where the pivot winds up
        TODO: rename/reformat to match wikipedia's names - https://en.wikipedia.org/wiki/Quicksort#Algorithm '''

    if not (start <= idx_pivot <= end):
        raise ValueError('idx pivot must be between start and end')

    # swap the pivot value with the first value the subarray of interest (start, end)
    array[start], array[idx_pivot] = array[idx_pivot], array[start]

    # track the pivot value
    pivot = array[start]
    
    # i is the storeIndex, j is the loopIndex. note that i <= j, always.
    i = start + 1
    j = start + 1

    # TODO: use xrange
    while j <= end:
        # if the loop index value is less than the pivot value,
        # move the loop value down into the less_than region
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            # advance the border of the less_than region
            i += 1
        # advance the low-value-seracher index
        j += 1

    # move the partition value where it belongs
    # the top of the less_than region
    array[start], array[i - 1] = array[i - 1], array[start]

    # let the parent function call know exactly where
    # the partial ordering vs. pivot holds
    return i - 1


def quicksort(array, start=0, end=None):
    if end is None:
        end = len(array) - 1
    if end - start < 1:
        return
    
    idx_pivot = random.randint(start, end)
    i = sub_partition(array, start, end, idx_pivot)
    
    quicksort(array, start, i - 1)
    quicksort(array, i + 1, end)
    return array


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

  

  assert tuple(quicksort_recursive(list(a0))) == a1
  assert tuple(quicksort_recursive_list_comprehension(list(a0))) == a1
  assert tuple(quicksort(list(a0))) == a1

  

  #
  import __main__
  print '\n*** Tests Pass ***\tfor file: {0}\n'.format(__main__.__file__)


if __name__ == '__main__':
    test()

