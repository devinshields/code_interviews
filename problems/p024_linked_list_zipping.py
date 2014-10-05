#!/usr/bin/env python
'''
---------------------------------------------------
PROBLEM STATEMENT:
---------------------------------------------------
  
  problem here

---------------------------------------------------

INPUTS:           x) a singly linked list

OUTPUTS:          x) singly linked list, but with its contents 'zipped'

CONSTRAINTS:      x) O(1) space constraint

OBJECTIVE:        x) produce a zipped list with minimal time complexity

ASSUMPTIONS:      x) no list loops or degenerate structure

TRADEOFFS:        x)


---------------------------------------------------
SOLUTIONS:
---------------------------------------------------
'''

class LinkedList(object):
  ''' '''
  class Node(object):
    def __init__(self, cargo=None, next_node=None):
      self.cargo = cargo
      self.next_node  = next_node
    def __str__(self):
      return 'Node({0})'.format(str(self.cargo))

  def __init__(self, collection=None):
    self.head = None
    # build from a source collections
    if collection:
      # build, then link nodes
      nodes = [self.Node(x) for x in collection]
      for p0, p1 in zip(nodes[:-1], nodes[1:]):
        p0.next_node = p1
      self.head = nodes[0]

  def as_generator(self):
    current_node = self.head
    while current_node:
      yield current_node
      current_node = current_node.next_node

  def __str__(self):
      return '[{0}]'.format(', '.join(map(str, self.as_generator())))




# test data
arr = range(5)
llist = LinkedList(arr)
print '\n', llist, '\n'


# IMPLEMENTATION

import itertools

def zip_linked_list(linked):
  '''  '''
  # iterate over the list to get the middle and last elements
  middle, last = linked.head, linked.head
  for i in itertools.count():
    print '\t', i, middle, last
    # break the loop when we hit the end
    if not last.next_node:
      break
    # otherwise advance the middle and last pointers, slow and fast respectively
    last = last.next_node
    if i % 2:
      middle = middle.next_node

  # starting at middle, reverse the node pointers
  zipper_prior, zipper_node = middle, middle.next_node
  
  # middle is the new tail when the list is odd length
  middle.next_node = None
  while zipper_node:
    print '\t', zipper_node
    # save a ref to the 'real' next node
    real_next = zipper_node.next_node
    zipper_node.next_node = zipper_prior
    zipper_node = real_next

  # start zippering
  first = linked.head
  while not first == middle:
    second = first.next_node
    tail_second = last.next_node
    # update the various node pointers
    first.next_node, last.next_node = last, second
    # iterate over the list
    first, last = second.next_node, tail_second
  return linked



# TEST DATA
print zip_linked_list(llist)


# TEST RUN


# EYEBALL SOLUTION



print
