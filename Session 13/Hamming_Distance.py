x=int(input("\nEnter the first integer = "))
y=int(input("\nEnter the second integer = "))
distance=bin(x^y).count('1')
print(f"\nHamming Distance = {distance}")

# Output
# Enter the first integer = 12
# Enter the second integer = 34
# Hamming Distance = 4