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


# import slingly linked list implementation



# IMPLEMENTATION

# TEST DATA

# TEST RUN

# EYEBALL SOLUTION


