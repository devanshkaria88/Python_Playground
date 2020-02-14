import secrets


def intake_string():  # Here the plain text is converted into the n bit Binary String
    plain_text = str(input("Enter your message"))  # Here we take the Plain text
    message_binary = ''.join(format(ord(i), 'b') for i in plain_text)
    print(message_binary)
    return message_binary


n = len(intake_string())


def key_generator(n):
    temp1 = []
    for j in range(0, n):
        b = str(secrets.randbelow(2))
        temp1.append(b)
    key = ''.join(temp1)  # Here the random key of the length of the n bit binary string is generated
    return key


print(key_generator(n))

# Key                                                               Message Text

# 1000001101001101001001101000001011110010101000110              1000100110010111101101100001110111011100111101000
# 0001010111101000111010000101110110101111011001000              1000100110010111101101100001110111011100111101000
# 1001001100101010100100010001101011001011010100111
