nums=list(map(int,input("\nEnter sorted array (comma-separated) = ").split(',')))
k=0
count=0
n=len(nums)
for i in range(n):
    if i<2 or nums[i]!=nums[k-2]:
        nums[k]=nums[i]
        k+=1
print(k)
print(nums[:k])

# Output
# Enter sorted array (comma-separated) = 1,1,1,2,2,3
# 5
# [1, 1, 2, 2, 3]