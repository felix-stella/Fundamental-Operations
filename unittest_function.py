import unittest
from function import Number,Fraction,Expression

def read_test_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

class TestNumber(unittest.TestCase):
    #def setUp(self):
    #    self.test_data = read_test_data('tests.txt')
    #    self.expected_results = read_test_data('expected_results.txt')

    def test_str(self):
        test_data = read_test_data('test_data/tests_str.txt')
        expected_results = read_test_data('test_data/expected_results_str.txt')
        for i, test_case in enumerate(test_data):
            nums = tuple(map(int, test_case.split(',')))
            num = Number(nums=nums)
            result = str(num)
            expected_result = expected_results[i]
            self.assertEqual(result, expected_result)

    def test_float(self):
        test_data = read_test_data('test_data/tests_float.txt')
        expected_results = read_test_data('test_data/expected_results_float.txt')
        for i, test_case in enumerate(test_data):
            nums = tuple(map(int, test_case.split(',')))
            num = Number(nums=nums)
            result = float(num)
            expected_result = float(expected_results[i])
            self.assertEqual(result, expected_result)

    def test_reduce_fraction(self):
        test_data = read_test_data('test_data/tests_reduce.txt')
        expected_results = read_test_data('test_data/expected_results_reduce.txt')
        for i, test_case in enumerate(test_data):
            nums = tuple(map(int, test_case.split(',')))
            num = Number(nums=nums)
            num.reduce_fraction()
            result = str(num)
            expected_result = expected_results[i]
            self.assertEqual(result, expected_result)

    def test_init(self):
        try:
            Number(nums=(1, 2))  # Should raise ValueError
        except ValueError as e:
            self.assertEqual(str(e), "nums must be a triplet (integer, numerator, denominator).")
        try:
            Number(nums=(1, 2, 0))  # Should raise ValueError
        except ValueError as e:
            self.assertEqual(str(e), "The denominator cannot be equal to 0.")
        try:
            Number(3.2)  # Should raise ValueError
        except ValueError as e:
            self.assertEqual(str(e), "max must be an integer and max must not be less than 1.")

class TestFractionClass(unittest.TestCase):

    def test_valid_initialization(self):
        test_data = read_test_data('test_data/tests_calculate.txt')
        expected_results = read_test_data('test_data/expected_results_calculate.txt')
        for i, test_case in enumerate(test_data):
            nums = test_case.split(',')
            num_1=Number(nums=(int(nums[0]),int(nums[1]),int(nums[2])))
            num_2=Number(nums=(int(nums[4]),int(nums[5]),int(nums[6])))
            op=nums[3]
            f=Fraction(num_1,num_2,op)
            result = str(f.calculate_fractions())
            expected_result = expected_results[i]
            self.assertEqual(result, expected_result)

    def test_subexpression_is_zero(self):
        num_1 = Number(nums=(1, 2, 3))
        num_2 = Number(nums=(0, 0, 3))
        f=Fraction(num_1,num_2,'%')
        try:
            result=f.calculate_fractions()
        except ValueError as e:
            self.assertEqual(str(e), "The divisor cannot be 0.")

class TestExpressionClass(unittest.TestCase):

    def test_calculate_answer(self):
        expression=Expression(10,10)
        exp_list_1=[[Number(nums=(0,3,2)),'+',Number(nums=(1,0,2))],['*',Number(nums=(5,0,2))],
                    ['%',Number(nums=(2,0,2))]]
        result_1=expression.calculate_answer(exp_list_1)
        expected_result_1=Number(nums=(6,1,4))
        self.assertEqual(str(result_1), str(expected_result_1))

        exp_list_2=[[Number(nums=(1,1,2)),'*',Number(nums=(1,3,2))],['%',Number(nums=(2,0,2))]]
        result_2=expression.calculate_answer(exp_list_2)
        expected_result_2=Number(nums=(1,7,8))
        self.assertEqual(str(result_2), str(expected_result_2))

        exp_list_3=[[Number(nums=(0,3,2)),'-',Number(nums=(1,0,2))],['*',Number(nums=(5,0,2))],
                    ['%',Number(nums=(2,0,2))]]
        try:
            result_3=expression.calculate_answer(exp_list_3)
        except ValueError as e:
            self.assertEqual(str(e),"Sub expression cannot be less than zero.")

        exp_list_4=[[Number(nums=(1,3,2)),'-',Number(nums=(1,0,2))],['-',Number(nums=(5,0,2))],
                    ['%',Number(nums=(2,0,2))]]
        try:
            result_4=expression.calculate_answer(exp_list_4)
        except ValueError as e:
            self.assertEqual(str(e),"Sub expression cannot be less than zero.")

if __name__ == '__main__':
    unittest.main()