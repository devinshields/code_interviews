#!/usr/bin/env python
'''
http://interactivepython.org/runestone/static/pythonds/Trees/heap.html
https://en.wikipedia.org/wiki/Binary_heap


Binary Heaps have 2 neat properties/requirements:
  - shape property. the tree is a complete binary tree.

  - Heap property. all nodes are either greater than or equal to
    or less than or equal to each of its children,
    according to a comparison predicate defined for the heap.

Can convert a list into a heap in linear time:
    - start at the middle element
    - call percolate_down()
    - decrement i
    - TODO: think about why this works.
            something to do with the binary tree structure and
            that percolation calls always pick the extremal child
'''

class BinaryHeap:
  ''' binary min-heap implementation '''
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0
  
  def percUp(self,i):
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]:
       tmp = self.heapList[i // 2]
       self.heapList[i // 2] = self.heapList[i]
       self.heapList[i] = tmp
      i = i // 2
  
  def insert(self,k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)

  def percDown(self,i):
    while (i * 2) <= self.currentSize:
      mc = self.minChild(i)
      if self.heapList[i] > self.heapList[mc]:
        tmp = self.heapList[i]
        self.heapList[i] = self.heapList[mc]
        self.heapList[mc] = tmp
      i = mc
  
  def minChild(self,i):
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
      if self.heapList[i*2] < self.heapList[i*2+1]:
        return i * 2
      else:
        return i * 2 + 1

  def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)
    return retval

  def buildHeap(self,alist):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while (i > 0):
      self.percDown(i)
      i = i - 1



def test():
  '''  '''

  # test data
  a0 = (9,5,6,2,3)


  # heapify
  bh = BinaryHeap()
  bh.buildHeap(list(a0))

  # test printing
  print
  print 'test data:', a0
  print 'as a heap:', bh.heapList
  print
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
  print(bh.delMin())
  print


if __name__ == '__main__':
  test()

