#!/usr/bin/env python
'''
https://class.coursera.org/algs4partI-006/quiz/attempt?quiz_id=90

Question 2
Stack with max. Create a data structure that efficiently supports
the stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are reals numbers so that you can compare them.


1) get a basic stack class set up
2) add the get-max function
3) think about the right data struct to track max

--

1) track the max value, rescan every time the max is popped

2) maintain a binary search tree with (key, value) -> (int, frequency)
   when a value is popped, search the tree and decrement that value

3) maintain a hash table from ints-to-frequency
   maintain a heap with the key - ..

4) REAL ANSWER:
    create a second stack to match the first and cache the current min there
    whenever there's an insert.

    http://stackoverflow.com/questions/3435926/insert-delete-max-in-o1

'''

class MaxStack(object):
  def __init__(self):
    self.stack = []
    self.maxes = []
  def push(self, val):
    self.stack.append(val)
    if not len(self.maxes):
      self.maxes.append(val)
    else:
      self.maxes.append(max(self.maxes[-1], val))
  def pop(self):
    self.maxes.pop()
    return self.stack.pop()
  def get_max(self):
    return self.maxes[-1]


def test():

  test_input = [1, 2, 3, 4, 3, 2, 1]

  stack = MaxStack()
  for i in test_input:
    stack.push(i)

  for i in test_input:
    print stack.get_max(), stack.pop()

  pass

if __name__ == '__main__':
  test()

