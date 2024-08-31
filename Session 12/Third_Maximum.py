nums=list(map(int,input("\nEnter the numbers separated by space = ").split()))
nums=list(set(nums)) 
nums.sort(reverse=True) 
if len(nums)<3:
    print(max(nums))
else:
    print(nums[2])

# Output
# Enter the numbers separated by space = 12 32 1
# 1