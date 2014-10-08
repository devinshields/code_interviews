#!/usr/bin/env python
'''
https://en.wikipedia.org/wiki/Heap_(data_structure)

  - Heap is a partially ordered data structure.
  - Nodes in a Heap Tree are garenteed to have consistent ordering between parents and children everywhere in the heap.
      - but no order is garenteed between siblings or cousins
  - frequently used in graph algorithms
  - sometimes used for sorting
  - uses array arithmetic for node relationships, needs an array to work

'''


import heapq


class MaxHeap(object):
  ''' simple max-heap implementation '''
  def __init__(self):
    self.arr = [None]
    self.N = 0
  def swim(self, k):
    while k > 1 and self.arr[k/2] < self.arr[k]:
      # swap
      self.arr[k], self.arr[k/2] = self.arr[k/2], self.arr[k]
      k = k/2
  def insert(self, val):
    self.arr.append(val)
    self.N += 1
    self.swim(self.N)
  def sink(self, k):
    ''' k is the index of the item that may need to sink. j is its child and potential swap-mate. '''
    while k*2 <= self.N:
      j = 2*k
      # pick the larger child of node k
      if j < self.N and self.arr[j] < self.arr[j+1]:
        j += 1
      # heap order is fixed, so quit
      if not self.arr[k] < self.arr[j]:
        break
      # swap
      self.arr[k], self.arr[j] = self.arr[j], self.arr[k]
      # advance the pointer
      k = j
  def delmax(self):
    cur_max = self.arr[1]
    self.arr[1] = self.arr.pop()
    self.N -= 1
    self.sink(1)
    return cur_max


def test():
  '''  '''

  max_heap = MaxHeap()

  for i in range(10):
    max_heap.insert(i)

  # freeze the test data
  max_heaped_arr = tuple(max_heap.arr[:1])

  # use the system libraries
  test_heap = list(max_heaped_arr)
  heapq._heapify_max(test_heap)

  assert max_heaped_arr == tuple(test_heap)



if __name__ == '__main__':
  test()

