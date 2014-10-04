#!/usr/bin/env python
'''
---------------------------------------------------
PROBLEM STATEMENT:
---------------------------------------------------
  
  problem here

---------------------------------------------------

INPUTS:           x) 

OUTPUTS:          x)

CONSTRAINTS:      x)

OBJECTIVE:        x)

ASSUMPTIONS:      x)

TRADEOFFS:        x)


---------------------------------------------------
SOLUTIONS:
---------------------------------------------------

use the postfix algorithm:
    https://en.wikipedia.org/wiki/Reverse_Polish_notation#Postfix_algorithm

---------------------------------------------------

'''


# test data
test0 = '3,4,*,1,2,+,+'
test1 = '1,1,+,-2,*'
test2 = '4,6,/,2,/'


cases = test0, test1, test2



# IMPLEMENTATION
import operator

def parse_calc_input(s):
  if s == '+':
    return operator.add
  elif s == '-':
    return operator.sub
  elif s == '*':
    return operator.mul
  elif s == '/':
    return operator.truediv
  else:
    return int(s)

def reverse_polish_calculator(input_string):
  # parse the string into values and operators
  input_tokens = map(parse_calc_input, input_string.split(','))

  #
  stack = []
  for token in input_tokens:
    # if it's a value
    if not hasattr(token, '__call__'):
      stack.append(token)
    else:
      # it's an operator
      y, x = stack.pop(), stack.pop()
      result = token(x, y)
      stack.append(result)

  # should be only 1 value in the stack for valid polish inputs
  assert len(stack) == 1
  return stack[0]


# TEST DATA
print map(reverse_polish_calculator, cases)


