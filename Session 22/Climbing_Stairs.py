n=int(input("\nEnter number of steps = "))
a,b=1,1
for _ in range(n-1):
    a,b=b,a+b
print(b)

# Output
# Enter number of steps = 5
# 8