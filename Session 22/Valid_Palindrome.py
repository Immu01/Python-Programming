s=input("\nEnter a string = ")
cleaned=''
for char in s:
    if char.isalnum():
        cleaned+=char.lower()
left=0
right=len(cleaned)-1
while left<right:
    if cleaned[left]!=cleaned[right]:
        print(False)
        break
    left+=1
    right-=1
else:
    print(True)

# Output
# Enter a string = A man, a plan, a canal: Panama
# True