#!/usr/bin/env python
'''
https://class.coursera.org/algs4partI-006/quiz/attempt?quiz_id=90

Question 1

Implement a queue with two stacks
so that each queue operations takes
a constant amortized number of stack operations.

------------

PLAN:

1) set up a queue class with two stacks
2) set up queue interface functions
3) work out 

'''


class StackQueue(object):
  def __init__(self):
    self.stack0 = []
    self.stack1 = []
  def enqueue(self, val):
    self.stack0.append(val)
  def dequeue(self):
    while self.stack0:
      self.stack1.append(self.stack0.pop())
    ret_val = self.stack1.pop()
    while self.stack1:
      self.stack0.append(self.stack1.pop())
    return ret_val


def test():

  test_input = 'hello, world!'

  queue = StackQueue()
  for c in test_input:
    queue.enqueue(c)

  try:
    while True:
      print queue.dequeue()
  except:
    pass

  pass

if __name__ == '__main__':
  test()

