import requests
from pwn import xor

def print_blk(hex_blks, sz):
   for i in range(0, len(hex_blks), sz):
       print(hex_blks[i:i+sz], ' ', end='')
   print()

# flag_encrypted = requests.get('https://aes.cryptohack.org/symmetry/encrypt_flag/').json()["ciphertext"]

# iv = flag_encrypted[0:32]
# cipher = flag_encrypted[32:]

# print(iv)
# print_blk(cipher, 32)


# zero_factor = '0'*32*3
# # print_blk(zero_factor, 32)
# # zero_factor = zero_factor.hex()

# # print(len(bytes.fromhex(zero_factor)))

# iv_encrypt = requests.get(f'https://aes.cryptohack.org/symmetry/encrypt/{zero_factor}/{iv}/').json()["ciphertext"]



# print_blk(iv_encrypt, 32)

# print(xor(bytes.fromhex(iv_encrypt), bytes.fromhex(cipher))) 


#OR Other solution
flag_encrypted = requests.get('https://aes.cryptohack.org/symmetry/encrypt_flag/').json()["ciphertext"]

iv = flag_encrypted[0:32]
cipher = flag_encrypted[32:]

flag = requests.get(f'https://aes.cryptohack.org/symmetry/encrypt/{cipher}/{iv}/').json()["ciphertext"]
print(bytes.fromhex(flag))
