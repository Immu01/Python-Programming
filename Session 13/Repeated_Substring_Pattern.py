s=input().strip()
l=len(s)
for i in range(1,l//2+1):
    if l%i==0:
        substring=s[:i]
        if substring*(l//i)==s:
            print("true")
            break
else:
    print("false")

# Output
# abab
# true