v12 = [
    88, 95, 38, 33, 111, 102, 113, 121, 123, 98,
    37, 122, 115, 75, 103, 109, 121, 118, 36, 120,
    75, 96, 117, 118, 120, 113, 33, 75, 125, 103,
    75, 32, 75, 119, 123, 121, 121, 36, 122, 75,
    102, 113, 98, 75, 96, 102, 37, 119, 127, 105
]

flag = ''.join(chr(x ^ 0x14) for x in v12)
print("Flag:", flag)
