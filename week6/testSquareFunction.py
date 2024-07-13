import unittest

class NotANumberError(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"{self.number} is not a number :/"
    

def square_function(number):
    if isinstance(number,(int,float)):
        return number*number
    else: 
        raise NotANumberError(number)
    

class TestSquare(unittest.TestCase):


    def test_invalid_input(self):
        with self.assertRaises(NotANumberError) as context:
            square_function("invalid")
        self.assertEqual(str(context.exception), "invalid is not a number :/")


    def test_square_values(self):
        result = square_function(4)
        self.assertEqual(result,16)


if __name__ == "__main__":
    unittest.main()
