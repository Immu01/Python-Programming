s=input("\nEnter a string of parentheses = ")
stack=[]
matching={')':'(','}':'{',']':'['}
for char in s:
    if char in matching.values():
        stack.append(char)
    elif char in matching:
        if stack and stack[-1]==matching[char]:
            stack.pop()
        else:
            print(False)
            break
else:
    print(not stack)

# Output
# Enter a string of parentheses = ()
# True