#To encode into base64, we turn string into bytes, then bytes into base64.

import base64

string_to_encode = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes = bytes.fromhex(string_to_encode)

b = base64.b64encode(bytes)

print(b)