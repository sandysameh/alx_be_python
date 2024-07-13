import unittest

def add(x,y):
    return x+y

class TestAdd(unittest.TestCase):

    def test_add_posittive(self):
        result = add(5,3)
        self.assertEqual(result,8)
    
    def test_neg_add(self):
        result = add(5,-7)
        self.assertEqual(result,-2)

if __name__ == "__main__":
    unittest.main()


    