l1=list(map(int,input("\nEnter first list (comma-separated) = ").split(',')))
l2=list(map(int,input("\nEnter second list (comma-separated) = ").split(',')))
def addTwoNumbers(l1,l2):
    l1.reverse()
    l2.reverse()
    carry=0
    result=[]
    while l1 or l2 or carry:
        val1=l1.pop(0) if l1 else 0
        val2=l2.pop(0) if l2 else 0
        total=val1+val2+carry
        carry=total//10
        result.append(total%10)
    result.reverse()
    return result
print(addTwoNumbers(l1,l2))

# Output
# Enter first list (comma-separated) = 7,2,4,3
# Enter second list (comma-separated) = 5,6,4
# [7, 8, 0, 7]