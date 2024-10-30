import unittest
from math_quiz import get_random_number, get_random_operator, generate_problem


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        for _ in range(1000):  # Test a large number of random operators
            oper = get_random_operator()
            self.assertTrue(oper in ['+', '-', '*'])

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (6, 2, '-', '6 - 2', 4),
            (6, 2, '*', '6 * 2', 12),
            # TODO: add more test cases if needed
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            
            # Generate the problem and answer using generate_problem
            problem, answer = generate_problem(num1, num2, operator)
            
            # Check that the generated problem and answer match the expected values
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

    def test_get_random_number_invalid_range(self):
        # Test that get_random_number raises ValueError if min > max
        with self.assertRaises(ValueError) as context:
            get_random_number(10, 1)
        
        # Check if the error message is correct
        self.assertEqual(str(context.exception), "min should not be greater than max")

   
                
                

if __name__ == "__main__":
    unittest.main()
