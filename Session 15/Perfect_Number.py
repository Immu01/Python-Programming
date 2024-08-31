n=int(input("\nEnter a positive integer = "))
if n<=1:
    print("false")
else:
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    if total==n:
        print("true")
    else:
        print("false")

# Output
# Enter a positive integer = 6
# true