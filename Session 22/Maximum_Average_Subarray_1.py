nums=[1,12,-5,-6,50,3]
k=4
max_sum=sum(nums[:k])
current_sum=max_sum
for i in range(k,len(nums)):
    current_sum+=nums[i]-nums[i-k]
    max_sum=max(max_sum,current_sum)
max_avg=max_sum/k
print(max_avg)

# Output
# 12.75