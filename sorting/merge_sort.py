#!/usr/bin/env python
'''
note: really fast on mostly sorted arrays
'''


def merge_sort(arr):

  def merge(arr, aux, lo, mid, hi):

    # NOTE: can speed this up a lot by using inertion sort
    #       when the array is small, i.e. around 7?   20% improvement
    
    # copy from the array to aux
    for k in range(lo, hi+1):
      aux[k] = arr[k]

    #
    i, j = lo, mid+1
    for k in range(lo, hi+1):
      if i > mid:
        arr[k] = aux[j]
        j += 1
      elif j > hi:
        arr[k] = aux[i]
        i += 1
      elif aux[j] < aux[i]:
        arr[k] = aux[j]
        j += 1
      else:
        arr[k] = aux[i]
        i += 1

  def sort(arr, aux, lo, hi):
    if hi <= lo:
      return
    mid = lo + (hi-lo)/2
    sort(arr, aux, lo, mid)
    sort(arr, aux, mid+1, hi)

    # NOTE can avoid the merge call if the two sub arrays are already sorted

    merge(arr, aux, lo, mid, hi)

  # initialize the auxilary array
  aux = [el for el in arr]

  # call the recursive sort
  sort(arr, aux, 0, len(arr)-1)

  return arr

def test():
  test_arr = list('hello, world')
  eval_arr = tuple(sorted(test_arr))

  #print eval_arr
  #print tuple(merge_sort(test_arr))

  assert eval_arr == tuple(merge_sort(test_arr))

  pass

if __name__ == '__main__':
  test()

