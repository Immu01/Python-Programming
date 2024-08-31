hex_map="0123456789abcdef"
num=int(input("\nEnter a number = "))
hex_num=""
while num>0:
    r=num%16
    num =num//16
    hex_num=hex_map[r]+hex_num
print(f"\nHexadecimal representation = {hex_num}")

# Output
# Enter a number = 123
# Hexadecimal representation = 7b