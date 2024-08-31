s=input("\nEnter 1st string = ")
t=input("\nEnter 2nd string = ")
s_count={}
for char in s:
    if char in s_count:
        s_count[char]+=1
    else:
        s_count[char]=1
for char in t:
    if char in s_count:
        s_count[char]-=1
    else:
        print(char)
        break

# Output
# Enter 1st string = abcd
# Enter 2nd string = bcde
# e