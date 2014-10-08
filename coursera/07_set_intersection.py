#!/usr/bin/env python
'''
https://class.coursera.org/algs4partI-006/quiz/attempt?quiz_id=79

Question 1 - Intersection of two sets.

  Given two arrays a[] and b[], each containing N distinct 2D points in the plane,
  design a subquadratic algorithm to count the number of points
  that are contained both in array a[] and array b[].  
'''


import random
random.seed(42)



def count_set_intersection(a, b):
  a.sort()
  b.sort()

  total = 0

  i, j, imax, jmax = 0, 0, len(a), len(b)

  while i < imax and j < jmax:
    if a[i] < b[j]:
      i += 1
    elif a[i] > b[j]:
      j += 1
    else: # a[i] == b[j]:
      total += 1
      i += 1
      j += 1
  return total


def test():

  # test data
  a = list(set([(random.randrange(10), random.randrange(10)) for i in range(100)]))
  b = list(set([(random.randrange(10), random.randrange(10)) for i in range(100)]))


  print count_set_intersection(list(a), list(b))
  print len(set(a) & set(b))

if __name__ == '__main__':
  test()

