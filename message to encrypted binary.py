message = input("Enter a message: ")
distance = int(input("Enter a distance value: "))
result = ""
for ch in message:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    shift = ""
    bitString = ""
    while cipherValue > 0:
        remainder = cipherValue % 2
        cipherValue = cipherValue // 2
        if cipherValue == 0:
            shift = str(remainder)
        else:
            bitString = str(remainder) + bitString
    result += bitString + shift + " "
print(result)
