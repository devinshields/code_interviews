#!/usr/bin/env python
'''

https://docs.python.org/2/library/collections.html#collections.deque

NOTE: use collections.deque

'''


class Queue(object):
  class Node(object):
    def __init__(self, cargo=None, next_node=None):
      self.next_node = next_node
      self.cargo = cargo
  def __init__(self):
    self.head = None
    self.tail = None
  def enqueue(self, cargo):
    new_node = self.Node(cargo)
    if self.tail:
      self.tail.next_node = new_node
      self.tail = new_node
    else:
      self.head = new_node
      self.tail = new_node
  def dequeue(self):
    ret_val = self.head
    self.head = ret_val.next_node
    return ret_val.cargo
      



def test():

  q = Queue()
  for i in range(10):
    q.enqueue(i)

  while q.head:
    print q.dequeue()



if __name__ == '__main__':
    test()

