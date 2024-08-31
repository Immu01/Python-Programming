n=int(input("\nEnter an integer = "))
if n<=0:
    print(False)
else:
    while n%4==0:
        n//=4
    print(n==1)

# Output
# Enter an integer = 16
# True