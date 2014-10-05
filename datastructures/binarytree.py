#!/usr/bin/env python
'''
enables translation from human readable tree info,
a list of tuples with relationships and node data,
and translates it into a BinaryTree

inspired by:
  http://code.activestate.com/recipes/286239-binary-ordered-tree/
'''


import collections


# let's make a simple input format for BinaryTrees. borrow from python graph formats:
#   https://www.python.org/doc/essays/graphs/

BinaryNodeTuple = collections.namedtuple('BinaryNodeTuple', ['name', 'cargo', 'left_name', 'right_name'])


class Node(object):
  def __init__(self, name=None, cargo=None, parent=None):
    self.name = name
    self.cargo = cargo
    self.left = None
    self.right = None
    self.parent = None
  def __str__(self):
    vals = [self.name, self.cargo, self.left and self.left.name, self.right and self.right.name]
    return 'Node(name={0}, cargo={1}, left_name={2}, right_name={3})'.format(*map(str, vals))
    

class BinaryTree(object):
  def __init__(self, node_graph=None):
    ''' builds a binary tree from a list of tuples representing nodes in the tree.
        assumes each tuple is a BinaryNodeTuple named tuple.
          warning: this code does not check if the graph you describe is a possible binary tree '''
    self.root = None
    # build a tree with graph tuples
    if node_graph:
      # build a node for each name observed
      name_to_node = dict()
      for t in node_graph:
        for name in [t.name, t.left_name, t.right_name]:
          if name and name not in name_to_node:
            name_to_node[name] = Node(name=name)
      # init all relationships within the graph tuples
      for parent_tup in node_graph:
        # get a node reference, update the cargo
        parent = name_to_node[parent_tup.name]
        parent.cargo = parent_tup.cargo
        # update left, right, and parent relationships
        if parent_tup.left_name:
          left = name_to_node[parent_tup.left_name]
          parent.left = left
          left.parent = parent
        if parent_tup.right_name:
          right = name_to_node[parent_tup.right_name]
          parent.right = right
          right.parent = parent
      # walk up the tree to find the root, assign it to the tree
      node = name_to_node.values()[0]
      while node.parent:
        node = node.parent
      self.root = node


def test():
  '''  '''

  # test data
  test_tree = [('A', 0, 'B', 'C'),
               ('B', 1, 'D', None),
               ('C', 2, None, None)]

  # named tuples from the raw node data
  node_graph = map(lambda t: BinaryNodeTuple(*t), test_tree)

  # build the tree
  tree = BinaryTree(node_graph=node_graph)

  # test print source
  print '\ngraph description for binary tree:'
  for t in node_graph:
    print t
  print

  # test print tree
  print 'graph as nodes in a tree:'
  print tree.root
  print '\t', tree.root.left
  print '\t\t', tree.root.left.left
  print '\t\t', tree.root.left.right
  print '\t', tree.root.right
  print '\t\t', tree.root.right.left
  print '\t\t', tree.root.left.right
  print

if __name__ == '__main__':
  test()

