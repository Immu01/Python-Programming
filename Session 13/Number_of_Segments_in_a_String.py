s=input().strip()
count=0
in_segment=False
for char in s:
    if char !=' ':
        if not in_segment:
            count+=1
            in_segment=True
    else:
        in_segment=False
print(count)

# Output
# Hello, my name is John
# 5