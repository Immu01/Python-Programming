s=input()
start=0
max_len=0
seen={}
for i in range(len(s)):
    if s[i] in seen and seen[s[i]]>=start:
        start=seen[s[i]]+1
    seen[s[i]]=i
    max_len=max(max_len,i-start+1)
print(max_len)

# Output
# abcabcbb
# 3