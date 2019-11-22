from questao01 import sum_to_target
import unittest

class TestaTipo(unittest.TestCase):
    def test_int(self):
        assert sum_to_target([2, 7, 11, 15], 9)

    def test_str(self):
       with self.assertRaises(TypeError):
           sum_to_target("abcd", 9)

    def test_tuple(self):
       with self.assertRaises(TypeError):
           sum_to_target((9, 9, 9), 9)

    def test_float(self):
       with self.assertRaises(TypeError):
           sum_to_target(9.5, 9)

class TestaResultado(unittest.TestCase):
    def test_normal(self):
        self.assertTrue(sum_to_target([2, 7, 11, 15], 9) == [0, 1])
    
    def test_diferente(self):
        self.assertTrue(not(sum_to_target([2, 7, 11, 15], 10)))
    
if __name__ == "__main__":
    unittest.main()