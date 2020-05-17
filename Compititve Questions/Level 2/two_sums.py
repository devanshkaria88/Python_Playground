"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

:::::::::Example::::::::

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

def solution(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: List[int]
    """

"""
print(solution([2,7,11,15], 9) should return [0,1]
print(solution([3,2,4], 6) should return [1,2]
print(solution([3,12,34,54,123], 37) should return [0,2]
print(solution([3,12,34,54,123], 37) should return [1,2]
print(solution([35,2312,434,1154,3123], 37) should return []
print(solution([1,1,1,1,1,4,42,12,43,42], 43) should return [0,6]
"""