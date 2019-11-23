from questao04 import calculate_rain
import unittest

class ReturnTest(unittest.TestCase):
    def test_return(self):
        self.assertIsInstance(calculate_rain([]), int)

class ResultTest(unittest.TestCase):
    def test_exemplo(self):
        self.assertEqual(calculate_rain([0,1,0,2,1,0,1,3,2,1,2,1]), 6)

    def test_empty(self):
        self.assertEqual(calculate_rain([0]), 0)

    def test_empty2(self):
        self.assertEqual(calculate_rain([]), 0)

class TypeTest(unittest.TestCase):
    def test_str(self):
        with self.assertRaises(TypeError):
            calculate_rain("7,1,5,3,6,4")

    def test_int(self):
        with self.assertRaises(TypeError):
            calculate_rain(7)
    
    def test_tuple(self):
        with self.assertRaises(TypeError):
            calculate_rain((7,1,5,3,6,4,))
    
    def test_float(self):
        with self.assertRaises(TypeError):
            calculate_rain(7.5)

    def test_float_inlist(self):
        with self.assertRaises(TypeError):
            calculate_rain([7,1,5,3,6,4.5])

if __name__ == "__main__":
    unittest.main()