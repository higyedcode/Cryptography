import requests
from datetime import datetime, timedelta
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from pwn import xor

# cookie_enc = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/').json()["cookie"]

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

# print_blk(cookie, 32)

# iv = cookie_enc[0:32]
# cookie = cookie_enc[32:]
# print_blk(iv, 32)
# print_blk(cookie, 32)

# rq = requests.get(f'https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}/').json()
# print(rq)
# expires_at = int((datetime.today() + timedelta(days=1)).timestamp())
# cookie = f"admin=False;expiry={expires_at}".encode()
# print_blk(cookie, 16)
# cookie = pad(cookie, 16)
# print_blk(cookie, 16)
# cookie = cookie.hex()
# print_blk(cookie, 32)


# d1 = xor(cookie[0:16], iv)
# print(d1)
# new_iv = xor(b'admin=True;expi', d1)
# print(new_iv.hex())
# print(xor(new_iv, d1))


#solve
cookie_enc = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/').json()["cookie"]

iv = bytes.fromhex(cookie_enc[0:32])
cookie_enc = cookie_enc[32:]

expires_at = int((datetime.today() + timedelta(days=1)).timestamp())
cookie = f"admin=False;expiry={expires_at}".encode()

print("iv ", iv)
d1 = xor(cookie[0:16], iv)
print("d1 ", len(d1))
new_iv = xor(b'admin=True;expir', d1)
print(len(new_iv))

print("New iv\n", new_iv)
print("Cookie enc\n", cookie_enc)

rq = requests.get(f'https://aes.cryptohack.org/flipping_cookie/check_admin/{cookie_enc}/{new_iv.hex()}/').json()
print(rq['flag'])