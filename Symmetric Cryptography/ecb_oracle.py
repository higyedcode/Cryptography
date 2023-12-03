
from Crypto.Cipher import AES
import requests
import time
import string

def encrypt(payload):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    r = requests.get(url + payload + '/')
    return r.json()['ciphertext']

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()


print('  ', end='')
print((bytes.hex(b'1'*15)))
print_blk(encrypt(bytes.hex(b'1'*15)), 32)

for i in range(ord('a'),ord('z')):    
    print(chr(i), '', end='')
    print_blk(encrypt(bytes.hex(b'1'*15+int.to_bytes(i, 1, 'little'))), 32)

def bruteforce():
    flag = 'crypto{'
    # flag=''
    total = 32 - 1
    alphabet = '_'+'@'+'{'+'}'+string.digits+string.ascii_lowercase+string.ascii_uppercase

    while True:
        payload = '1' * (total-len(flag))
        expected = encrypt(payload.encode().hex())
        print('E', '', end='')
        print_blk(expected, 32)
        
        for c in alphabet: 
            res = encrypt(bytes.hex((payload + flag + c).encode()))
            print(c, '', end='')
            print_blk(res, 32)
            if res[32:64] == expected[32:64]:
                flag += c
                print(flag)
                break
            # time.sleep(1)

        if flag.endswith('}'): break

    print(flag)

# bruteforce()