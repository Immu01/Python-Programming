head=list(map(int,input("\nEnter linked list (comma-separated) = ").split(',')))
k=int(input("\nEnter k-Value = "))
if not head:
    print([])
else:
    n=len(head)
    k=k%n
    if k==0:
        print(head)
    else:
        rotated_list=head[-k:]+head[:-k]
        print(rotated_list)

# Output
# Enter linked list (comma-separated) = 1,2,3,4,5
# Enter k-Value = 2
# [4, 5, 1, 2, 3]
