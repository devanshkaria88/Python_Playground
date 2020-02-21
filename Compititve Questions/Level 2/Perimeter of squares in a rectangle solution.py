def fib(n):
    a, b = 0, 1

    for i in range(n + 1):
        if i == 0:
            yield b
        else:
            a, b = b, a + b
            yield b


def perimeter(n):
    return sum(fib(n)) * 4
