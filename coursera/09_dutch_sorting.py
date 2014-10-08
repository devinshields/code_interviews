#!/usr/bin/env python
'''
https://class.coursera.org/algs4partI-006/quiz/attempt?quiz_id=79

Question 3
  Dutch national flag. Given an array of N buckets, each containing a red, white, or blue pebble, sort them by color.
  The allowed operations are:
    swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
    color(i): color of pebble in bucket i.
  The performance requirements are as follows:
    At most N calls to color().
    At most N calls to swap().
    Constant extra space.

'''


import random
random.seed(42)


# constraint counters
calls_to_color, calls_to_swap = 0, 0



def sort_dutch(arr):
  
  def color(i):
    calls_to_color += 1
    return arr[i]

  def swap(i, j):
    calls_to_swap += 1
    arr[i], arr[j] = arr[j], arr[i]
  
  # index invariants: red, white, unkn, blue
  #      red zone:      arr[0:red]
  #      white zone:    arr[red:white]
  #      unknown:       arr[white:blue]
  #      blue zone:     arr[blue:N]
  red, white, blue, N = 0, 0, len(arr), len(arr)

  # iterate over arr, call color(), and move the value to the right zone
  while white < blue:
    
    white += 1

  return arr



def test():
  colors = ['r', 'w', 'b']

  test_array = tuple(colors[random.randrange(3)] for i in range(10))

  def color_key(c):
    return colors.index(c)

  print sort_dutch(list(test_array))
  print sorted(test_array, key=color_key)

  print 
  print calls_to_color, calls_to_swap, len(test_array)

  assert calls_to_color < len(test_array)
  assert calls_to_color < len(test_array)



if __name__ == '__main__':
  test()

