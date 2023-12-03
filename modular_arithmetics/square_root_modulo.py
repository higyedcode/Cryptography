# for i in range(30):
#     if (i*i)%29 == 6:
#         print(i)
#         break

p = 29
ints = [14, 6, 11]

qr = [a for a in range(p) if pow(a,2,p) in ints]
print(f"flag is {qr}")