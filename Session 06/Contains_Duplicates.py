def has_duplicates(lst):
    seen=set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False
my_list = [1,2,3,4,2]
print(has_duplicates(my_list))
my_list2=[1,2,3,4]
print(has_duplicates(my_list2))

# Output
# True
# False