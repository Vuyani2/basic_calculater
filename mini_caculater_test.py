import unittest
from main import add



class TestAdd(unittest.TestCase):

    def test_add(self):
        a_method = add()
        self.assertEqual(2, a_method.add(1, 1), "adding 1 to 1 should be 2")




