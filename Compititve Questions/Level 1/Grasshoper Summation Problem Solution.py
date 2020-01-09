"""
Write a program that finds the summation of every number from 1 to num.
The number will always be a positive integer greater than 0.
"""


def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum = sum + i
    return sum


print(summation(1))  # should return 1
print(summation(13))  # should return 91
print(summation(153))  # should return 11781
print(summation(34))  # should return 595
print(summation(23))  # should return 276
print(summation(8))  # should return 36
print(summation(4))  # should return 10
print(summation(3))  # should return 6
print(summation(65))  # should return 2145
