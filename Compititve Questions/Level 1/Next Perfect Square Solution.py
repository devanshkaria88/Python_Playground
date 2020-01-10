def find_next_square(sq):
    if (sq ** 0.5) % 1 == 0:
        a = sq ** 0.5
        return (a + 1) ** 2
    else:
        return -1


print(find_next_square(121))  # This Should return 144
print(find_next_square(625))  # This Should return 676
print(find_next_square(169))  # This Should return 196
print(find_next_square(319225))  # This Should return 320356
print(find_next_square(400))  # This Should return 441
print(find_next_square(25))  # This Should return 36
print(find_next_square(15241383936))  # This Should return 15241630849
print(find_next_square(39))  # This Should return -1
