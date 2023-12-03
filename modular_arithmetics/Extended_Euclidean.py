def gcd_extended(a,b):
    if a == 0:
        return b, 0, 1
    
    gcd, s1, t1 = gcd_extended(b%a, a)

    s,t = updateCoefficients(a,b,s1,t1)
    return gcd, s,t
    
def updateCoefficients(a,b,s,t):
    return (t - (b//a)*s,s)
'''
25 = 10*2 + 5
10 = 5*2 + 0

-------
0*0 + 1*5 = 5, s1 = 0, s2 = 1
0*(10-5*2) + 1*5 = 5 <==> 0+1*(25-10*2) =25 - 2*1-
--------------

81, 57
81 = 1*57 + 24
57 = 2*24 + 9
24 = 2*9 + 6
9 = 1*6 + 3
6 = 2*3 + 0

0*0 + 3*1 = 3, s1 = 0, s2 = 1, a= 0, b = 3
1*(9-1*6) = 3 <==>9 - 1*6, s1 = s2, s2 = t - s1*(b//a)
'''

# print(gcd_extended(26513,32321))

# print(11%6)
# print(8146798528947 % 17)

'''
3
'''
# print(pow(3,19)%17)
# print(pow(5,17)%17)
# print(pow(7,17)%17)


print(pow(3,11) % 13)
