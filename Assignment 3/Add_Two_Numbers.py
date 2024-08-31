l1=[2,4,3]
l2=[5,6,4]
carry=0
result=[]
max_len=max(len(l1),len(l2))
for i in range(max_len):
    digit1=l1[-1-i] if i<len(l1) else 0
    digit2=l2[-1-i] if i<len(l2) else 0
    total=digit1+digit2+carry
    result.append(total%10)
    carry=total//10
if carry>0:
    result.append(carry)
result.reverse()
print(result)

# Output
# [8, 0, 7]