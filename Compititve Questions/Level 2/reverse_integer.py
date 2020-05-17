"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21

:::: NOTE ::::
Assume we are dealing with an environment which could only store integers within the
32-bit signed integer range: [−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def solution(x):
    """
    :param x: int
    :return: int
    """

"""
print(solution(123)) should return 321
print(solution(-123)) should return -321
print(solution(123431519129)) should return 0
print(solution(1231243)) should return 3421321
print(solution(123456789)) should return 987654321
print(solution(1234567809)) should return 0
"""