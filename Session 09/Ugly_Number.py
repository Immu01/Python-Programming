n=int(input("\nEnter an integer = "))
if n<=0:
    print(False)
else:
    for p in [2,3,5]:
        while n%p==0:
            n//=p
    print(n==1)

# Output
# Enter an integer = 6
# True