nums=list(map(int,input("\nEnter sorted array elements separated by spaces = ").split()))
target=int(input("\nEnter the target value = "))
left,right=0,len(nums)-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print(left)

# Output
# Enter sorted array elements separated by spaces = 1 3 5 6
# Enter the target value = 5
# 2