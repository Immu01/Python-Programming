n=int(input("\nEnter an integer = "))
if n<=0:
    print(False)
else:
    while n%3==0:
        n//=3
    print(n==1)

# Output
# Enter an integer = 243
# True