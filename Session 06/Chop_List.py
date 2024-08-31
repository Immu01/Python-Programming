def chop(lst):
    if len(lst)>1:
        del lst[0]
        del lst[-1]
    elif len(lst)==1:
        del lst[0]
my_list=[1,2,3,4,5]
chop(my_list)
print(my_list)

# Output
# [2, 3, 4]