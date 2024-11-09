import unittest
from math_quiz import random_int, random_operator, calculate

class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random_operator() returns a valid operator
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Run the test 1000 times to ensure randomness
            operator = random_operator()
            self.assertIn(operator, valid_operators)  # Check that the operator is one of the valid options

    def test_calculate(self):
        # Test if calculate() function returns correct problems and answers
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (9, 3, '-', '9 - 3', 6),
            (4, 6, '*', '4 * 6', 24),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = calculate(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
