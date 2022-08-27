'''
bitwise operator convert the numbers into bit then do the operation and = & , or = | , xor = ^
bin() function is converted to see the bit representation of decimal number
'''


x = 10
y = 8

print(bin(x))
print(bin(y))

print(x & y, bin(x & y))
print(x | y, bin(x | y))
print(x ^ y, bin(x ^ y))

