nums=input("\nEnter numbers separated by spaces = ").split()
nums=[str(num) for num in nums]
sorted_nums=sorted(nums,key=lambda x:x*10,reverse=True)
result=''.join(sorted_nums)
print("\nOutput = ",result.lstrip('0')or'0')

# Output
# Enter numbers separated by spaces = 10 2
# Output =  210