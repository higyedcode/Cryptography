from pwn import *

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key12 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flagkey123 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
key1b = bytes.fromhex(key1)
key12b = bytes.fromhex(key12)
key23b = bytes.fromhex(key23)
flagkey123b = bytes.fromhex(flagkey123)

key2 = xor(key1b, key12b)
key3 = xor(key2, key23b)
flag = xor(flagkey123b, key1b, key2, key3)


#other solution
flag2 = xor(flagkey123b,key1b, key23b)

print(flag2)
print(flag)

print(len(key1))
print(len(flag))