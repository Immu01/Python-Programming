nums=list(map(int,input("\nEnter numbers separated by spaces = ").split()))
n=len(nums)
total_sum=n*(n+1)//2
current_sum=sum(nums)
missing_number=total_sum-current_sum
print(missing_number)

# Output
# Enter numbers separated by spaces = 3 0 1
# 2