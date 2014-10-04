#!/usr/bin/env python
'''

INPUTS:       x) an array 'A' with comparable elements
              x) an index 'i' into the array

OUTPUTS:      x) a partially sorted array

OBJECTIVE:    x) reorder 'A' into 3 groups
                  - initial elements <  A[i]
                  -         elements == A[i]
                  -         elements >  A[i]

SUBJECT TO:   x) O(1) space complexity

'''


# make up test data
A0, i0 = (4, 3, 7, 5, 9, 1, 0, 6), 3



# IMPLEMENTATION
def partial_sort(A, i):
  ''' TODO '''
  return A



# test
def comparator(x, y):
  ''' custom comparitor function for this special problem instance '''
  if x < y: return -1
  if y < x: return 1
  return 0


def test_partial_sort(A, i):
  ''' compare A with A[i] then group the resulting comparisons.
      the ordered keys must match one of the asserted patters to be valid. '''
  
  compared = [comparator(x, A[i]) for x in A]
  import itertools
  unique_keys =  tuple(k for k, grp in itertools.groupby(compared))

  assert unique_keys == (-1, 0, 1) or unique_keys == (-1, 0) or unique_keys == (0, 1) or unique_keys == (0)


test_partial_sort(partial_sort(list(A0), i0), i0)


