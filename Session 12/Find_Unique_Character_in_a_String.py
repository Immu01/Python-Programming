s=input("\nEnter a string = ")
char_count={}
for char in s:
    if char in char_count:
        char_count[char]+=1
    else:
        char_count[char]=1
for char,count in char_count.items():
    if count==1:
        print(f"\nUnique character = {char}")
        break

# Output
# Enter a string = leetcode
# Unique character = l