def solution(x):
    """
    :type x: int
    :rtype: int
    """
    if (x > (-2 ** 31) and x < (2 ** 31 - 1)):
        if x >= 0:
            x = str(x)
            x = list(x)
            x.reverse()
            b = ''.join(x)
            if -2 ** 31 < int(b) < (2 ** 31 - 1):
                return int(b)
            else:
                return 0
        else:
            a = ['-']
            x = str(x)
            x = x.lstrip("-")
            x = list(x)
            x.reverse()
            a.extend(x)
            b = ''.join(a)
            if -2**31 < int(b) < (2**31-1):
                return int(b)
            else:
                return 0
    else:
        return 0

print(solution(1234567809))