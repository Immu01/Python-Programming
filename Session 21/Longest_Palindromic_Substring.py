s=input()
start=0
max_len=1
def expand_around_center(left,right):
    while left>=0 and right<len(s) and s[left]==s[right]:
        left-=1
        right+=1
    return left+1,right-1
for i in range(len(s)):
    l1,r1=expand_around_center(i,i)
    l2,r2=expand_around_center(i,i+1)
    if r1- 1>max_len:
        start=l1
        max_len=r1-l1
    if r2-l2>max_len:
        start=l2
        max_len=r2-l2
print(s[start:start+max_len+1])

# Output
# babad
# bab