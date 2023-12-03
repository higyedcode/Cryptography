import requests


BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
cipher_text = data["ciphertext"]
print("ciphertext", cipher_text)

r = requests.get(f"{BASE_URL}/decrypt/{cipher_text}/")
cipher_decoded = r.json()["plaintext"]
print("plaintext",bytes.fromhex(cipher_decoded))
