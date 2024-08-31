def is_power(a,b):
    if b<=1:
        return a==b
    if a<b:
        return False
    if a==b:
        return True
    if a%b==0:
        return is_power(a//b,b)
    return False
print(is_power(27,3))
print(is_power(16,2))
print(is_power(20,2))
print(is_power(81,3))

# Output
# True
# True
# False
# True