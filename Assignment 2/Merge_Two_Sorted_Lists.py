list1=list(map(int,input("\nEnter elements of list1 separated by spaces = ").split()))
list2=list(map(int,input("\nEnter elements of list2 separated by spaces = ").split()))
merged=[]
i,j=0,0
while i<len(list1) and j<len(list2):
    if list1[i]<list2[j]:
        merged.append(list1[i])
        i+=1
    else:
        merged.append(list2[j])
        j+=1
while i<len(list1):
    merged.append(list1[i])
    i+=1
while j<len(list2):
    merged.append(list2[j])
    j+=1
print(merged)

# Output
# Enter elements of list1 separated by spaces = 1 2 4
# Enter elements of list2 separated by spaces = 1 3 4
# [1, 1, 2, 3, 4, 4]