import unittest
from src.arrays import *


#helpers


class TestArrays(unittest.TestCase):
  
  #every
  def test_1(self):
    print('Check every value in array equal 5')
    self.assertTrue(every([5,5,5,5], lambda val: val == 5 ), 'error message here')

  def test_2(self):
    print('Check every value in array does not equal 7')
    self.assertFalse(every([5,5,6,7], lambda val: val == 7 ), 'error message here')

  #some
  def test_some1(self):
    print('Check some value in array equals 5')
    self.assertTrue(some([4,5,6,7], lambda val: val == 5 ), 'error message here')

  def test_some2(self):
    print('Check some value in array does not equal 7')
    self.assertFalse(some([5,5,6,8], lambda val: val == 7 ), 'error message here')


suite = unittest.TestLoader().loadTestsFromTestCase(TestArrays)
unittest.TextTestRunner(verbosity=2).run(suite)
