#!/usr/bin/env python
'''
---------------------------------------------------
PROBLEM STATEMENT:
---------------------------------------------------
  
  problem here

---------------------------------------------------

INPUTS:           x) binary tree representing lockable resources

OUTPUTS:          x) API with 3 functions:
                        - isLock()
                        - lock()
                        - unLock()

CONSTRAINTS:      x) a node can not be locked if any of its children or ancestors are locked
                  x) isLock() -> O(1) time complexity
                     lock()   -> O(h) time complexity, h is the height of a node
                     unLock   -> O(h) ime complexity, h is the height of a node

OBJECTIVE:        x) minimize space complexity while satisfying the constraints

ASSUMPTIONS:      x)

TRADEOFFS:        x)


---------------------------------------------------
SOLUTIONS:
---------------------------------------------------

BRUTE FORCE:      x)

ANY PATTERNS?:    x)

REFINED:          x)

EVEN BETTER:      x)

CASES:            x)

CAVEATS:          x)

---------------------------------------------------

'''

# import binary tree, add locking and counting logic
class Node(object):
  def __init__(self):
    # relationships
    self.left = None
    self.right = None
    self.parent = None
    # lock tracking
    self.is_locked = False
    self.children_locked = 0
  def isLock(self):
    return self.is_locked
  def lock(self):
    # check if already locked
    if self.is_locked:
      raise Exception('this node already locked!')
    # check if any children are locked
    if self.children_locked > 0:
      raise Exception('child nodes are locked, cannot lock this node')
    # check if ancestors are locked
    node = self
    while node.parent:
      node = node.parent
      if node.isLock():
        raise Exception('an ancestors node is locked, cannot lock this node')
    # all conditions met, update the lock state
    self.is_locked = True
    # +1 to children_locked for all ancestors
    node = self
    while node.parent:
      node = node.parent
      node.children_locked += 1
  def unlock(self):
    ''' undo everything done in lock() '''
    # check if already unlocked
    if not self.is_locked:
      raise Exception('this node already unlocked!')
    self.is_locked = False
    # -1 to children_locked for all ancestors
    node = self
    while node.parent:
      node = node.parent
      node.children_locked -= 1
  def __str__(self):
    return 'Node(locked:{0}, children_locked:{1})'.format(self.is_locked, self.children_locked)



# *** TODO: needs real testing ***


# build a test tree
n0 = Node()

print
print n0
print n0.isLock()
print n0.lock()
print n0.unlock()
print n0
print 


# IMPLEMENTATION

# TEST DATA

# TEST RUN

# EYEBALL SOLUTION



