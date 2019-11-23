from questao03 import find_max_profit
import unittest

class ReturnTest(unittest.TestCase):
    def test_return(self):
        self.assertIsInstance(find_max_profit([]), int)

class ResultTest(unittest.TestCase):
    def test_exemplo1(self):
        self.assertEqual(find_max_profit([7,1,5,3,6,4]), 5)

    def test_exemplo2(self):
        self.assertEqual(find_max_profit([7,6,4,3,1]), 0)

class TypeTest(unittest.TestCase):
    def test_str(self):
        with self.assertRaises(TypeError):
            find_max_profit("7,1,5,3,6,4")

    def test_int(self):
        with self.assertRaises(TypeError):
            find_max_profit(7)
    
    def test_tuple(self):
        with self.assertRaises(TypeError):
            find_max_profit((7,1,5,3,6,4,))
    
    def test_float(self):
        with self.assertRaises(TypeError):
            find_max_profit(7.5)

    def test_float_inlist(self):
        with self.assertRaises(TypeError):
            find_max_profit([7,1,5,3,6,4.5])

if __name__ == "__main__":
    unittest.main()