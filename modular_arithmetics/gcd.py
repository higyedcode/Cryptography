def gcd(a,b):
    while a%b!=0:
        rest = a%b
        a = b
        b = rest
    return b

def gcd1(a,b):
    while a != b:
        if a > b:
            a -= b
        elif b > a:
            b -= a
    return b

print(gcd(66528,52920))
print(gcd1(66528,52920))