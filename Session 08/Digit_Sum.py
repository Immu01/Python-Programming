num=int(input("\nEnter an integer = "))
while num>=10:
    total=0
    while num>0:
        total+=num%10
        num//=10
    num=total
print(f"\nThe sum of digits = {num}")

# Output
# Enter an integer = 1234
# The sum of digits = 1