def cumsum(numbers):
    cumulative_sum=[]
    total=0
    for num in numbers:
        total+=num
        cumulative_sum.append(total)
    return cumulative_sum
my_list=[1,2,3,4]
result=cumsum(my_list)
print(result)

# Output
# [1, 3, 6, 10]