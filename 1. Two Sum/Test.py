import unittest
from Solution import twoSum


class TestTwoSum(unittest.TestCase):
    def testcase1(self):
        nums = [2, 7, 11, 15]
        target = 9
        actual = twoSum(nums, target)
        expected = [0, 1]
        self.assertEqual(set(actual), set(expected))

    def testcase2(self):
        nums = [3, 2, 4]
        target = 6
        actual = twoSum(nums, target)
        expected = [1, 2]
        self.assertEqual(set(actual), set(expected))

    def testcase3(self):
        nums = [3, 3]
        target = 6
        actual = twoSum(nums, target)
        expected = [0, 1]
        self.assertEqual(set(actual), set(expected))


if __name__ == '__main__':
    unittest.main()
