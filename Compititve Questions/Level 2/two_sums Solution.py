def solution(nums, target):
    for i in nums:
        for j in range(nums.index(i) + 1, len(nums)):
            if (i + nums[j] == target):
                return \
                    [nums.index(i), j]

"""
This is a naive approach to the problem with the complexity of O(n^2)..
As there were no time constraints given to the solution, this works fairly well.
"""