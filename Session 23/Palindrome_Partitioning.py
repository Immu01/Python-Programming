s=input("\nEnter a string = ")
result=[]
n=len(s)
stack=[(0,[])]
while stack:
    start,path=stack.pop()
    if start==n:
        result.append(path)
    for end in range(start+1,n+1):
        substring=s[start:end]
        if substring==substring[::-1]:
            stack.append((end,path+[substring]))
print(result)

# Output
# Enter a string = aab
# [['aa', 'b'], ['a', 'a', 'b']]