nums=list(map(int,input("\nEnter sorted array (comma-separated) = ").split(',')))
target=int(input("\nEnter target value = "))
left,right=0,len(nums)-1
firstPos=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        firstPos=mid
        right=mid- 1
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
left,right=0,len(nums)-1
lastPos=-1
while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        lastPos=mid
        left=mid+1
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
print([firstPos,lastPos])

# Output
# Enter sorted array (comma-separated) = 5,7,7,8,8,10
# Enter target value = 8
# [3, 4]