from questao01 import sum_to_target
import unittest

class TypeTest(unittest.TestCase):
    def test_list(self):
        self.assertIsInstance(sum_to_target([2, 7, 11, 15], 9), list)

    def test_str(self):
       with self.assertRaises(TypeError):
           sum_to_target("abcd", 9)

    def test_int(self):
       with self.assertRaises(TypeError):
           sum_to_target(1, 9)

    def test_tuple(self):
       with self.assertRaises(TypeError):
           sum_to_target((9, 9, 9), 9)

    def test_float(self):
       with self.assertRaises(TypeError):
           sum_to_target(9.5, 9)

class SecondParameterTypeTest(unittest.TestCase):
    def test_str(self):
       with self.assertRaises(TypeError):
           sum_to_target([1, 2], "3")

    def test_tuple(self):
       with self.assertRaises(TypeError):
           sum_to_target([1, 2], (3,))

    def test_float(self):
       with self.assertRaises(TypeError):
           sum_to_target([1, 2], 3.4)

    def test_list(self):
       with self.assertRaises(TypeError):
           sum_to_target([1, 2], [3])

class TestaResultado(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sum_to_target([2, 7, 11, 15], 9), [0, 1])
    
    def test_diferente(self):
        self.assertEqual(sum_to_target([2, 7, 11, 15], 10), None)
    
if __name__ == "__main__":
    unittest.main()