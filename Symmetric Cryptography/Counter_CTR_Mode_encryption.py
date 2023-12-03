from Crypto.Cipher import AES
import os
import requests
from pwn import xor

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
       print()


class StepUpCounter(object):
    def __init__(self, value=os.urandom(16), step_up=False):
        self.value = value.hex()
        self.step = 1
        self.stup = step_up

    def increment(self):
        if self.stup:
            self.newIV = hex(int(self.value, 16) + self.step)
        else:
            self.newIV = hex(int(self.value, 16) - self.stup)
        self.value = self.newIV[2:len(self.newIV)]
        return bytes.fromhex(self.value.zfill(32))

    def __repr__(self):
        self.increment()
        return self.value
    
cipher = requests.get("https://aes.cryptohack.org/bean_counter/encrypt/").json()["encrypted"]
# print_blk(cipher, 32)
# print(len(cipher)//32 + 1)
# print(hex(892))
# val = b'f'*16
# print(val)
# print(len(val.hex()))

PNG_header = bytes([0x89, 0x50,0x4e,0x47,0x0d,0x0a,0x1a,0x0a,0x00, 0x00, 0x00,0x0d, 0x49, 0x48, 0x44, 0x52])

iv = xor(PNG_header,bytes.fromhex(cipher[0:32]))
print(iv)

flag = b''
for i in range(0, len(cipher), 32):
    flag+=(xor(bytes.fromhex(cipher[i:i+32]), iv))

with(open('flag.png', 'wb')) as f:
    f.write(flag)
print(flag)