def remove_smallest(numbers):
    a = numbers[:]
    if len(numbers) > 0:
        a.remove(min(a))
        return a
    else:
        return numbers


print(remove_smallest([112, 12, 433, 44, 25]))  # Should return [112, 433, 44, 25]
print(remove_smallest([]))  # Should return []
print(remove_smallest([1325, 1324, 54, 12, 5, 0, 213]))  # Should return [1325, 1324, 54, 12, 5, 213]
print(remove_smallest([34, 123, 54, 12, 98, 12, 4, 6, 6, 6, 6, 34, 213, 4,
                       2]))  # Should return [34, 123, 54, 12, 98, 12, 4, 6, 6, 6, 6, 34, 213, 4]
print(
    remove_smallest([34, 123, 76, 12, 0, 0, 0, 0, 0, 324, 12]))  # Should return [34, 123, 76, 12, 0, 0, 0, 0, 324, 12]
print(remove_smallest([1]))  # Should return []
print(remove_smallest([2]))  # Should return []
print(remove_smallest([2, 2, 2, 2, 2, 2, 2]))  # Should return [2, 2, 2, 2, 2, 2]
print(remove_smallest([12, 12, 3, 1, 2, 3, 5, 1, 2, 23, 4]))  # Should return [12, 12, 3, 2, 3, 5, 1, 2, 23, 4]
print(remove_smallest([98, 45, 87, 34, 87, 23, 78, 23]))  # Should return [98, 45, 87, 34, 87, 78, 23]
print(remove_smallest([123, 45, 2, 3, 3, 12, 54, 23, 3, 4, 1]))  # Should return [123, 45, 2, 3, 3, 12, 54, 23, 3, 4]
print(remove_smallest([12, 23, 12, 43, 12, 43, 1, 243, ]))  # Should return [12, 23, 12, 43, 12, 43, 243]
