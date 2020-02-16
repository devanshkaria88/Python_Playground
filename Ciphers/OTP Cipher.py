import secrets


def otp_cipher():
    message = str(input("Enter your message"))
    encryption(message)


def encryption(message):
    message_binary = ''.join(format(ord(i), 'b') for i in message)
    temp1 = []
    for j in range(0, len(message_binary)):
        b = str(secrets.randbelow(2))
        temp1.append(b)
    key = ''.join(temp1)  # Here the random key of the length of the n bit binary string is generated
    temp2 = []
    for i in range(0, len(key)):
        if message_binary[i] == key[i]:
            temp2.append('0')
        else:
            temp2.append('1')
    cipher_text = ''.join(temp2)
    print("Message binary is: " + message_binary)
    print("Random key is: " + key)
    print("Encrypted message is: " + cipher_text)
    decryption(cipher_text, key)


def decryption(cipher_text, key):
    temp3 = []
    for i in range(0, len(key)):
        if cipher_text[i] == key[i]:
            temp3.append('0')
        else:
            temp3.append('1')
    recieved_text = ''.join(temp3)
    print("The binary string that reciever will get is: " + recieved_text)


otp_cipher()
