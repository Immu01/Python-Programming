strs=["eat","tea","tan","ate","nat","bat"]
groups={}
for s in strs:
    key=''.join(sorted(s))
    if key not in groups:
        groups[key]=[]
    groups[key].append(s)
print(list(groups.values()))

# Output
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]