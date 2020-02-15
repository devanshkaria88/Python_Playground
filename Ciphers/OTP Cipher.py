import secrets

plain_text = 'Devansh'  # Here we take the Plain text
message_binary = ''.join(format(ord(i), 'b') for i in plain_text)
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
temp3 = []
for i in range(0, len(key)):
    if cipher_text[i] == key[i]:
        temp3.append('0')
    else:
        temp3.append('1')
recieved_text = ''.join(temp3)
print(message_binary)
print(key)
print(cipher_text)
print(recieved_text)
