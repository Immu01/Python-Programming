height=[1,8,6,2,5,4,8,3,7]
max_area=0
left=0
right=len(height)-1
while left<right:
    width=right-left
    area=min(height[left],height[right])*width
    max_area=max(max_area,area)
    if height[left]<height[right]:
        left+=1
    else:
        right-=1
print(max_area)

# Output
# 49