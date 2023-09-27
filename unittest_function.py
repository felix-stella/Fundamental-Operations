import unittest
from function import Number

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

if __name__ == '__main__':
    unittest.main()