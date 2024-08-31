a=input("\nEnter first binary string = ")
b=input("\nEnter second binary string = ")
max_len=max(len(a),len(b))
a=a.zfill(max_len)
b=b.zfill(max_len)
carry=0
result=[]
for i in range(max_len-1,-1,-1):
    total=int(a[i])+int(b[i])+carry
    result.append(str(total%2))
    carry=total//2
if carry:
    result.append('1')
print(''.join(result[::-1]))

# Output
# Enter first binary string = 11
# Enter second binary string = 1
# 100