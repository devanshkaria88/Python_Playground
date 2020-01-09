def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


print(is_triangle(1, 1, 3))
print(is_triangle(3, 4, 4))
print(is_triangle(4, 5, 1))
print(is_triangle(5, 7, 5))
print(is_triangle(11, 9, 9))
print(is_triangle(3, 8, 5))
print(is_triangle(9, 4, 9))
print(is_triangle(4, 2, 6))
print(is_triangle(6, 3, 12))
