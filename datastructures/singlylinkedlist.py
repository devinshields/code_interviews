#!/usr/bin/env python
''' http://www.openbookproject.net/thinkcs/python/english2e/ch18.html
    note: might want to make this a real data structure? iterable, etc.?
    
---------------------
NOTE: you can make any python iterable into a single linked list by using:
          iter() and next()

      for example:


arr = range(5)

iter0 = iter(arr)
iter1 = iter(arr)

print next(iter0), next(iter0), next(iter0), next(iter1) 
    
'''


class Node(object):
  '''  '''
  def __init__(self, cargo=None, next_node=None):
    self.cargo = cargo
    self.next_node  = next_node
  def __str__(self):
    return 'Node({0})'.format(str(self.cargo))


class LinkedList(object):
  ''' for a mature API, look at the list docs for python and Java:
          https://docs.python.org/2/tutorial/datastructures.html#more-on-lists
          http://docs.oracle.com/javase/7/docs/api/java/util/List.html  '''
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


def test():
  '''  '''

  # build some linked nodes
  n2 = Node(2)
  n1 = Node(1, n2)
  n0 = Node(0, n1)

  # and print to test
  print LinkedList(n0), '\n'
  print LinkedList(), '\n'
  print LinkedList(collection=range(5)), '\n'


if __name__ == '__main__':
  test()

