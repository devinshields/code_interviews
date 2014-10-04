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

BRUTE FORCE:      x) make a generating function that produces the indices that need swapping
                  x) feed each index 2-tuple to a swap function, iterating over the list for each swap

ANY PATTERNS?:    x)

REFINED:          x) forward iterate over the list once and
                     use loop counters to calculate link distance to the next swap node.
                     continue until hitting the half way point node.

EVEN BETTER:      x) find the list center with a slow pointer following a fast pointer.
                     store as the halting condition.
                  x) move 2 pointers inside an iteration loop, swap, and continue.                   

CASES:            x) even # of nodes
                  x) odd # of nodes

CAVEATS:          x)

---------------------------------------------------

'''


# import linked list
class Node(object):
  def __init__(self, cargo=None, next_node=None):
    self.cargo = cargo
    self.next_node  = next_node
  def __str__(self):
    return 'Node({0})'.format(str(self.cargo))


class LinkedList(object):
  def __init__(self, head=None, collection=None):
    if head and collection:
      raise
    # build from 1 head node
    self.head = head
    # or from a source collections
    if collection:
      # build, then link nodes
      nodes = [Node(x) for x in list(collection)]
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
arr = range(6)
link_list = LinkedList(arr)

print '\ntest data:', arr, link_list, '\n'

link0 = iter(arr)
link1 = iter(arr)

# IMPLEMENTATION

# TEST DATA

# TEST RUN

# EYEBALL SOLUTION


