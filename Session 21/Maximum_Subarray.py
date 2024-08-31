nums=list(map(int,input("\nEnter array (comma-separated) = ").split(',')))
max_sum=float('-inf')
current_sum=0
for num in nums:
    current_sum=max(num,current_sum+num)
    max_sum=max(max_sum,current_sum)
print(max_sum)

# Output
# Enter array (comma-separated) = -2,1,-3,4,-1,2,1,-5,4
# 6