list1=list(map(int,input("\nEnter integers for the first list (comma-separated) = ").split(',')))
list2=list(map(int,input("\nEnter integers for the second list (comma-separated) = ").split(',')))
same_length=len(list1)==len(list2)
same_sum=sum(list1)==sum(list2)
common_values=set(list1)&set(list2)
print(f"\nSame length = {same_length}")
print(f"\nSame sum = {same_sum}")
print(f"\nCommon values = {list(common_values)}" if common_values else "\nNo common values")

# Output
# Enter integers for the first list (comma-separated) = 1,2,3,4,5 
# Enter integers for the second list (comma-separated) = 2,3,4,5,6
# Same length = True
# Same sum = False
# Common values = [2, 3, 4, 5]