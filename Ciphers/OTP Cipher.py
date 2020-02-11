a = 'Hello'
res = ''.join(format(ord(i), 'b') for i in a)
print(res)
print(len(res))
