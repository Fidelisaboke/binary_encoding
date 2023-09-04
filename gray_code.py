def gray_code(binary_num):
    bits = []
    for i in range(len(binary_num)):
        if i == 0:
            bits.append(binary_num[i])
        else:
            bits.append(str(int(binary_num[i]) ^ int(binary_num[i - 1])))
    return ''.join(bits)


# testing
print(gray_code('0001'))
print(gray_code('0100'))
print(gray_code('1000'))