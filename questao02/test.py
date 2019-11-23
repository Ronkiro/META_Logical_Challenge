from questao02 import is_balanced
import unittest

class ResultTest(unittest.TestCase):
    def test_padrao(self):
        self.assertEqual(is_balanced("{[()]}"), "SIM")
    
    def test_falha(self):
        self.assertEqual(is_balanced("{[(])}"), "NÃO")

    def test_complexo(self):
        self.assertEqual(is_balanced("{{[[(())]]}}"), "SIM")

    def test_complexo(self):
        self.assertEqual(is_balanced("31232132312"), "SIM")

    def test_complexo(self):
        self.assertEqual(is_balanced("31232132312{"), "NÃO")

class TypeTest(unittest.TestCase):
    def test_padrao(self):
        self.assertIsInstance(is_balanced("{{[[(())]]}}"), str)

    def test_list(self):
        with self.assertRaises(TypeError):
            is_balanced(["{{[[(())]]}}"])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            is_balanced(("{{[[(())]]}}",))

    def test_int(self):
        with self.assertRaises(TypeError):
            is_balanced(1231231232)

if __name__ == "__main__":
    unittest.main()