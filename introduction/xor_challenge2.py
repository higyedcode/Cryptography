
# from pwn import xor


# msg = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# # result = xor(key[:7],"crypto{")
# # print(result.decode())

# #result is myXORke -> we assume the key is myXORkey repeated n times

# partialKey = "myXORkey"

# # completeKey = (partialKey * (len(msg)+1))[:len(msg)]
# # print(completeKey)

# # flag = xor(msg, completeKey)
# flag =xor(msg, 'myXORkey'.encode())

# print(flag)

from pwn import xor


msg = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

print(xor(msg, "crypto{".encode()))
print(xor(msg, "myXORkey".encode()))

#xor does go back to the beginning of string if the end of the string is met!