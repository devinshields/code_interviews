#!/usr/bin/env python
'''  '''


def int_to_binary_string(i, bit_length=8):
  ''' converts an int into a bit string representing the binary
      values for a unsigned int. pads with 0s up to the desired bit length. '''
  bin_string = bin(i)[2:]
  if len(bin_string) < bit_length:
    bin_string = '0' * (bit_length - len(bin_string)) + bin_string
  return bin_string


def binary_string_to_integer(bin_string):
    ''' inverse of int_to_binary_string '''
    return int(bin_string, 2)


def int_to_binary_string_twos_compliment(i):
    ''' TODO '''
    raise NotImplementedError('need to do this')


def test():
  ''' unit tests for utility functions '''

  #
  assert int_to_binary_string(253) == '11111101'
  assert binary_string_to_integer(int_to_binary_string(253)) == 253

  assert int_to_binary_string_twos_compliment(4)

  #

  import __main__
  print '\n*** Tests Pass ***\tfor file: {0}\n'.format(__main__.__file__)

if __name__ == '__main__':
  test()

