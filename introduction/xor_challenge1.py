from pwn import xor

key = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

for i in range(128):
    print(chr(i))
    print(xor(key,i), "\n")

print(len(key))


# from pwn import xor

# key = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

# for i in range(128):
#     result =  xor(key,i)
#     if result.find(bytes('crypto','UTF-8')) != -1 :
#         print(result, "\n")



