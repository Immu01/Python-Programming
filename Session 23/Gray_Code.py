n=2
result=[]
for i in range(2**n):
    result.append(i^(i>>1))
print(result)

# Output
# [0, 1, 3, 2]