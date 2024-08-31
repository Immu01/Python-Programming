nums=list(map(int,input("\nEnter sorted array elements separated by spaces = ").split()))
if not nums:
    print(0)
else:
    k=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1
    print(k)
    print(nums[:k])

# Output
# Enter sorted array elements separated by spaces = 1 1 2
# 2
# [1, 2]