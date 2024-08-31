s=input("\nEnter a string = ")
result=""
for char in s:
    if 'A'<=char<='Z':
        result+=chr(ord(char) + 32)
    else:
        result+=char
print(f"\nLowercase string = {result}")

# Output
# Enter a string = HellO
# Lowercase string = hello