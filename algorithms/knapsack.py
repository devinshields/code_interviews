#!/usr/bin/env python
'''
http://rosettacode.org/wiki/Knapsack_problem/Unbounded/Python_dynamic_programming
'''

def knapsack_unbounded_dp(items, C):
    '''
    items - a collections, each member representing an item's: (value, weight)
    C     - an int representing total knapsack capacity
    '''
    # order by max value per item size
    items = sorted(items, key=lambda item: item[VALUE]/float(item[SIZE]), reverse=True)
 
    # Sack keeps track of max value so far as well as the count of each item in the sack
    sack = [(0, [0 for i in items]) for i in range(0, C+1)]   # value, [item counts]
 
    for i,item in enumerate(items):
        name, size, value = item
        for c in range(size, C+1):
            sackwithout = sack[c-size]  # previous max sack to try adding this item to
            trial = sackwithout[0] + value
            used = sackwithout[1][i]
            if sack[c][0] < trial:
                # old max sack with this added item is better
                sack[c] = (trial, sackwithout[1][:])
                sack[c][1][i] +=1   # use one more
 
    value, bagged = sack[C]
    numbagged = sum(bagged)
    size = sum(items[i][1]*n for i,n in enumerate(bagged))
    # convert to (iten, count) pairs) in name order
    bagged = sorted((items[i][NAME], n) for i,n in enumerate(bagged) if n)
 
    return value, size, numbagged, bagged


def main():
  pass

if __name__ == '__main__':
  main()

