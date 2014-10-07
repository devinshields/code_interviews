#!/usr/bin/env python
'''
https://class.coursera.org/algs4partI-006/quiz/attempt?quiz_id=90

Question 4
Detect cycle in a linked list. A singly-linked data structure is a data structure made up of nodes where each node has a pointer to the next node (or a pointer to null). Suppose that you have a pointer to the first node of a singly-linked list data structure:
Determine whether a singly-linked data structure contains a cycle. You may use only two pointers into the list (and no other variables). The running time of your algorithm should be linear in the number of nodes in the data structure.
If a singly-linked data structure contains a cycle, determine the first node that participates in the cycle. you may use only a constant number of pointers into the list (and no other variables). The running time of your algorithm should be linear in the number of nodes in the data structure.
You may not modify the structure of the linked list.

---

1) make a singly linked list class
2) make a testing function - use racetrack algorithm
3) make test data

'''

import itertools

class LinkedList(object):
  def __init__(self):
    self.next_node = None




def linked_list_has_loop(llist):
  ''' set up two iterators, a fast and a slow.
      if fast is null, return False
      if fast == slow at any point, return True
  '''
  slow, fast = llist, llist.next_node
  for i in itertools.count(1):
    if not fast:
      return False
    if slow == fast:
      return True
    # otherwise, advance the counters
    if i%2:
      fast = fast.next_node
    else:
      fast = fast.next_node
      slow = slow.next_node
  




def test():
  nodes = [LinkedList() for i in range(5)]
  for i, n in enumerate(nodes[:-1]):
    n.next_node = nodes[i+1]
  no_loop = nodes[0]

  # verify the setup
  #print nodes[0], nodes[-1], nodes[-1].next_node


  nodes = [LinkedList() for i in range(5)]
  for i, n in enumerate(nodes):
    n.next_node = nodes[(i+1)%len(nodes)]
  loop = nodes[0]

  # verify the loop
  #print nodes[0], nodes[-1], nodes[-1].next_node
  #print

  print linked_list_has_loop(no_loop)
  print linked_list_has_loop(loop)


if __name__ == '__main__':
  test()

