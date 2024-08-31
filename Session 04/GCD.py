def gcd(a,b):
    a,b=abs(a),abs(b)
    while b!=0:
        a,b=b,a%b
    return a
print(gcd(48,18))
print(gcd(56,98))
print(gcd(101,10))

# Output
# 6
# 14
# 1