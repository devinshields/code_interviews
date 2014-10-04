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


# IMPLEMENTATION
def partial_sort(A, i):
  ''' maintain 4 groups with 3 index pointers:
        pointers: smaller, equal, larger
        groups:   bottom, middle, unknown, top

      ranges are index inclusive:
        bottom range:     0       to (smaller-1)
        middle range:     smaller to (equal-1)
        unknown range:    equal   to (larger-1)
        top range:        larger  to len(A)-1

      iterate over the each element in the array,
      swapping unknown elements into a known group,
      then updating pointers
  '''
  # initalize pivot value and group pointers
  pivot = A[i]
  smaller, equal, larger = 0, 0, len(A)

  print 'pivot:', pivot, 'A:', A
  print
  print

  #
  while equal < larger:
    print smaller, equal, larger, A
    # A[equal] is the current unknown element
    if A[equal] < pivot:
      # swap with the first of the middle range
      temp = A[smaller]
      A[smaller] = A[equal]
      A[equal] = temp

      # +1 bottom and middle pointers
      smaller += 1
      equal +=1

    elif A[equal] == pivot:
      # do nothing, but advance the equal counter
      equal += 1

    else:
      # swap with the last element of the unknown range
      temp = A[larger-1]
      A[larger-1] = A[equal]
      A[equal] = temp

      # -1 the larger pointer
      larger -= 1

    print smaller, equal, larger, A
    print
  return A


# TEST DATA
A0, i0 = (4, 3, 7, 5, 9, 1, 0, 6), 2


# TEST EYEBALL
print partial_sort(list(A0), i0)












'''
# REAL TESTING
def comparator(x, y):
  '' custom comparitor function for this special problem instance ''
  if x < y: return -1
  if y < x: return 1
  return 0


def test_partial_sort(A, i):
  '' compare A with A[i] then group the resulting comparisons.
      the ordered keys must match one of the asserted patters to be valid. ''
  
  compared = [comparator(x, A[i]) for x in A]
  import itertools
  unique_keys =  tuple(k for k, grp in itertools.groupby(compared))

  assert unique_keys == (-1, 0, 1) or unique_keys == (-1, 0) or unique_keys == (0, 1) or unique_keys == (0)

test_partial_sort(partial_sort(list(A0), i0), i0)

'''
