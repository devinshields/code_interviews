#!/usr/bin/env python
'''
http://en.wikipedia.org/wiki/Heapsort
http://rosettacode.org/wiki/Sorting_algorithms/Heapsort#Python

notes: 1) max heapify an array
       2) while heap.size() > 0,
          pop the max value and push it an index at the end of the heap
          move the last element in the heap to the root and call sink()
       3) once this starts, all elements at the end of the array are 
          sorted - this is the invariant.

'''


def heapsort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  # in pseudo-code, heapify only called once, so inline it here
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 
def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break



def test():
  
  # test data
  a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
  a0, a1 = tuple(a), tuple(sorted(a))

  assert tuple(heapsort(list(a0))) == a1

  print '\nsuccess!\n'


if __name__ == '__main__':
    test()

