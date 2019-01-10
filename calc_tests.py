import unittest
from calc import add, subtract, multiply, division

class CalculatorTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(4, add(2,2))
        self.assertEqual(5, add(2,3))

    def testDivision(self):
        self.assertEqual(1, division(1,1))
        self.assertEqual(1, division(2,2))
        self.assertEqual(2, division(2,1))
        self.assertEqual(3, division(7.5, 2.5))
    
    
    def testMultiply(self):
        self.assertEqual(4, multiply(2,2))
        self.assertEqual(9, multiply(3,3))

    def testSubtract(self):
        self.assertEqual(0, subtract(2,2))
        self.assertEqual(1, subtract(3,2))
        
unittest.main()
