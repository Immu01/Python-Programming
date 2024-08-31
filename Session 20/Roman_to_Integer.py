s=input("\nEnter a Roman numeral = ")
values={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
total=0
prev_value=0
for char in s:
    value=values[char]
    if value>prev_value:
        total+=value-2*prev_value
    else:
        total+=value
    prev_value=value
print(total)

# Output
# Enter a Roman numeral = III
# 3