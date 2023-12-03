import requests
import hashlib
import sys
import binascii
from Crypto.Cipher import AES


print("YEAH")
cipher_text = requests.get("https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/").json()["ciphertext"]


with open("Symmetric Cryptography\passwds.txt") as f:
    count = 0
    for word in f:
        count += 1
        word = word.strip()
        key = hashlib.md5(word.encode()).hexdigest()
        # plaintext = bytes.fromhex(requests.get(f"https://aes.cryptohack.org/passwords_as_keys/decrypt/{cipher_text}/{key}/").json()["plaintext"])
        ciphertext = bytes.fromhex(cipher_text)
        key = bytes.fromhex(key)

        cipher = AES.new(key, AES.MODE_ECB)
        try:
            decrypted = cipher.decrypt(ciphertext)
            # result = binascii.unhexlify(decrypted.hex())
            result = bytes(decrypted)
            if result.startswith('crypto{'.encode()) :
                print(count)
                print(result)
                sys.exit(0)

        except ValueError as e:
            continue

