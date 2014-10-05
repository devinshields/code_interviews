#!/usr/bin/env python
'''
http://www.reddit.com/r/cscareerquestions/comments/1z97rx/from_a_googler_the_google_interview_process
http://thereq.com/q/best-python-software-interview-questions/google
'''


# reverse a string in place
def reverse_string_in_place(s):
  ''' takes a python string and reverses them in place (as much as possible in python) '''
  s = list(s)
  start, end = 0, len(s)-1
  while start < end:
    s[start], s[end] = s[end], s[start]
    start += 1
    end -= 1
  return ''.join(s)

assert reverse_string_in_place('hello, world!') == 'hello, world!'[::-1]



# implement atoi
def atoi(s):
  char_to_digit = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
  total, mult, chars = 0, 0, list(s)
  while chars:
    total += char_to_digit[chars.pop()] * 10**mult
    mult += 1
  return total

assert atoi('5329') == 5329




# reverse a linked list
class Node(object):
  def __init__(self, next_node=None):
      self.next_node = next_node

def reverse_linked_list(head):
  first, second = head, head.next_node
  first.next_node = None
  while second:
    temp0, temp1 = second, second.next_node
    second.next_node = first
    first, second = temp0, temp1
  return first

h0 = Node(Node(Node()))
#print h0, h0.next_node, h0.next_node.next_node
h1 = reverse_linked_list(h0)
#print h1, h1.next_node, h1.next_node.next_node



# case-insensitive string comparison
def case_insensitive_string_comparison(s0, s1):
  return s0.lower() == s1.lower()




# recursive function to reverse a string
def string_reverse_recursive(s):
  # base case, empty string
  if not s:
    return ''
  return string_reverse_recursive(s[1:]) + s[:1]


print string_reverse_recursive('hello, world!')






def main():
  pass

if __name__ == '__main__':
  main()

