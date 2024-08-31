nums=list(map(int,input("\nEnter numbers separated by spaces = ").split()))
target=int(input("\nEnter the target number = "))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            print([i,j])
            break
    else:
        continue
    break

# Output
# Enter numbers separated by spaces = 2 7 11 15 
# Enter the target number = 9
# [0, 1]