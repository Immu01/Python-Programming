n=int(input("\nEnter an integer = "))
a,b=0,1
for _ in range(n):
    a,b=b,a+b
print(f"\nFibonacci number = {a}")

# Output
# Enter an integer = 4
# Fibonacci number = 3