def isPalindromeintonly(x):
    """
    :type x: int
    :rtype: bool
    """
    if (x > 0):
        temp = x
        b = 0
        while (x > 0):
            digit = x % 10
            b = b * 10 + digit
            x = x // 10
        if (b == temp):
            return 'true'
        else:
            return 'false'
    else:
        return 'false'


def ispalindromestr(x):
    return str(x) == str(x)[::-1]


print(isPalindromeintonly(-121))