import unittest
from funcoes import soma

class TestFuncoes(unittest.TestCase):
    def test_soma_dois_inteiros(self):
        self.assertEqual(soma(1, 2), 3)
        self.assertEqual(soma(-1, 1), 1)
        self.assertEqual(soma(0, 0), 0)
