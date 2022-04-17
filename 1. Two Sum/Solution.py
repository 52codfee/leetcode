from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    Args:
        nums (List[int]): An array of integers
        target (int): An integer target

    Returns:
        List[int]: Indices of the two numbers that add up to target
    """

    index_map = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in index_map.keys():
            return [index_map[diff], i]
        else:
            index_map[nums[i]] = i
