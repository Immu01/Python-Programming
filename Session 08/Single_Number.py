nums=list(map(int,input("\nEnter the numbers separated by spaces = ").split()))
single_number=0
for num in nums:
    single_number^=num
print(single_number)

# Output
# Enter the numbers separated by spaces = 1 2 3 3 2 4 5 4 5
# 1