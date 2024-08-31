list1=input("\nEnter the first list of words (comma-separated) = ").split(',')
list2=input("\nEnter the second list of words (comma-separated) = ").split(',')
set1=set(list1)
set2=set(list2)
difference=set1-set2
print(list(difference))

# Output
# Enter the first list of words (comma-separated) = apple,banana,orange,grape 
# Enter the second list of words (comma-separated) = banana,grape
# ['orange', 'apple']