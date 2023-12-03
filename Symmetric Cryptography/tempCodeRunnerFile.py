
f1 = xor(iv_encrypt[0:32], cipher[0:32])
f2 = xor(iv_encrypt[32:64], cipher[32:64])
f3 = xor(iv_encrypt[64:], cipher[64:])
print(f1+f2+f3)