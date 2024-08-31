s=input("\nEnter the first string = ")
goal=input("\nEnter the second string = ")
if len(s)!=len(goal):
    print("false")
else:
    doubled_s=s+s
    if goal in doubled_s:
        print("true")
    else:
        print("false")

# Output
# Enter the first string = abcde
# Enter the second string = cdeab
# true