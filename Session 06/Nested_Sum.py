def nested_sum(nested_list):
    total=0
    for sublist in nested_list:
        for num in sublist:
            total+=num
    return total
nested_list=[[1,2,3],[4,5],[6]]
print(nested_sum(nested_list))

# Output
# 21