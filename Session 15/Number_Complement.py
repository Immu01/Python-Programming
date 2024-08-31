num=int(input("\nEnter an integer = "))
bit_length=num.bit_length()
mask=(1<<bit_length)-1
complement=mask^num
print(f"\nComplement = {complement}")

# Output
# Enter an integer = 12
# Complement = 3