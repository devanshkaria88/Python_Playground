def oddOrEven(arr):
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 == 0:
        return "even"
    else:
        return "odd"


print(oddOrEven([0, 1, 2, 4, 1, 3, 4, 5, 6, 8, 9, 0, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0]))  # It should return even
print(oddOrEven([0, 1, 23, 4345641, 21123, 1242, 13, 23, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 1, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 261]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 2411, 3, 244, 5, 6, 8, 9989, 0, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2214, 4, 1, 3, 4, 5, 6, 8, 9, 0, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2, 424, 1, 341, 4, 5, 6, 8, 9, 99880, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2, 4, 1, 3124, 4, 5, 6, 8, 9, 0, 2, 14232, 13, 23, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 1, 43, 4, 5, 6, 8, 9, 0, 2, 6335443478912, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2, 4421, 1, 3, 4, 5, 6, 898, 9, 0, 2, 175472982, 13, 23, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 1, 4212143, 4, 5, 6, 8, 9, 0, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2, 4, 1, 3, 4421, 5, 6, 878, 9, 0, 2, 12, 107324693, 23, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 1, 3, 4, 5, 4216, 8, 9, 0, 2, 12, 13, 23, 1, 21]))  # It should return odd
print(oddOrEven([0, 1, 2, 4, 1, 3, 487, 5, 6, 14528, 9, 0, 2, 12, 13, 21423, 1, 21]))  # It should return even
print(oddOrEven([0, 1, 2, 4, 1, 3, 4, 534, 6, 8, 9, 0, 2, 12, 13, 23, 1, 21]))  # It should return even
