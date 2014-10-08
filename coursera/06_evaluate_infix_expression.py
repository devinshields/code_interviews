#!/usr/bin/env python
'''
http://stackoverflow.com/questions/13421424/how-to-evaluate-an-infix-expression-in-just-one-scan-using-stacks


Dijkstra's two stack algorithm:

  1) ignore left parenthesis
  2) push values to value stack
  3) push operand to operand stack
  4) right parens, double pop values, pop operand, evaluate, push to value stack
  5) at the end, should only be one value in the val stack. return it.
'''


import operator


def evaluate_infix_expression(expression):
  ''' assumes picky input format. doesn't handle negative values. '''
  val_stack, op_stack = [], []
  
  op_map = {'+':operator.add,
            '-':operator.sub,
            '*':operator.mul,
            '/':operator.truediv}

  for s in expression.split():
    if s == '(':
      continue
    elif s.isdigit():
      val_stack.append(int(s))
    elif s in op_map:
      op_stack.append(op_map[s])
    elif s == ')':
      y, x = val_stack.pop(), val_stack.pop()
      op = op_stack.pop()
      val_stack.append(op(x, y))
    else:
      raise
  
  #
  assert len(op_stack) == 0
  assert len(val_stack) == 1
  
  return val_stack.pop()

def test():
  test_expression = '( 2 + ( 5 * 4 ) )'

  print test_expression
  print '\t=', evaluate_infix_expression(test_expression)

  pass

if __name__ == '__main__':
  test()

