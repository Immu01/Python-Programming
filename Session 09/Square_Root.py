x=float(input("\nEnter a number = "))
root=x
epsilon=0.0001
while abs(root*root-x)>=epsilon:
    root=(root+x/root)/2
print(f"\nThe square root of {x} = {root}")

# Output
# Enter a number = 5
# The square root of 5.0 = 2.2360688956433634