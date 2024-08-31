nums=list(map(int,input("\nEnter numbers separated by spaces = ").split()))
nums.sort()
max_product=max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
print(f"\nMaximum product of three numbers = {max_product}")

# Output
# Enter numbers separated by spaces = 1 2 3 
# Maximum product of three numbers = 6