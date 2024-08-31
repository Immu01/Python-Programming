strs=input("\nEnter strings separated by commas = ").split(',')
if not strs:
    print("")
else:
    prefix=strs[0]
    for s in strs[1:]:
        i=0
        while i<len(prefix) and i<len(s) and prefix[i]==s[i]:
            i+=1
        prefix=prefix[:i]
        if not prefix:
            break
    print(prefix)

# Output
# Enter strings separated by commas = flower,flow,flight
# fl