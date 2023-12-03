
msg = "label"
characters = [ord(c) for c in msg]
encoded_chars = [c^13 for c in characters]
encoded_msg = ""

for c in encoded_chars:
    encoded_msg += chr(c)

print(encoded_msg)


