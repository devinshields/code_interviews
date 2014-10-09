#!/usr/bin/env python
'''  '''


def BFS(s, adj):
  '''  '''
  level = {s:0}
  parent = {s:None}
  i, frontier = 1, [s]
  while frontier:
    next = []
    for u in frontier:
      for v in adj[u]:
        if v not in level:
          level[v] = i
          parent[v] = u
          next.append(v)
    frontier = next
    i += 1
  # show results
  print
  for t in level.items():
    print t


def test():
  s = 0
  adj = {0:[1, 2], 1:[2], 2:[4], 3:[0], 4:[3, 0]}

  BFS(s, adj)

  pass

if __name__ == '__main__':
  test()

