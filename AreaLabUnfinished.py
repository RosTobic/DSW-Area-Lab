import math #math library has code to do math
import unittest

def circleArea(radius): 
    """return the area of a circle"""
    return math.pi * radius * radius

def rectArea(base, height):
    """return the area of a rect"""
    return base * height

def trapArea(base1, base2, height):
    """return the area of a trap"""
    return  height * (base1 + base2) / 2

def triArea(base,height):
    """return the area of a tri"""
    return base * height / 2
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertAlmostEqual(circleArea(5),25*math.pi)
    def testRectArea(self):
        self.assertAlmostEqual(rectArea(5,5),25)
    def testTrapArea(self):
        self.assertAlmostEqual(trapArea(5,5,5),25)
    def testTriArea(self):
        self.assertAlmostEqual(triArea(5,5),12.5)