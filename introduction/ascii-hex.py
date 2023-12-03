b = b'crypto{You_will_be_working_with_hex_strings_a_lot}' # this makes it a string of bytes

c = b.hex()
a = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

#b = bytes.fromhex(a) #converts a hexadecimal number into a string of bytes which can be printed and interpreted as string

#print(b)

print(a)
print(c)
print(a == c)