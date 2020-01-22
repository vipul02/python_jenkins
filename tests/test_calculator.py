from unittest import TestCase
from src.calculator import add

class TestCalc(TestCase):

    def setUP(self):
        pass

    def test_1(self):
        expected = 6
        actual = add(3, 3)
        self.assertEqual(expected, actual)
    
    def test_2(self):
        expected = 10
        actual = add(1, 9)
        self.assertEqual(expected, actual)
    
    def test_3(self):
        expected = 2
        actual = add(1, 1)
        self.assertEqual(expected, actual)
    
    def test_4(self):
        expected = 6
        actual = add(1, 1)
        self.assertNotEqual(expected, actual)
