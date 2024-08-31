n=int(input("\nEnter the N value = "))
pos=[]
neg=[]
for i in range(n):
    num=int(input(f"\nEnter the number {i+1} = "))
    if num>=0:
        pos.append(num)
    else:
        neg.append(num)
print(f"\nThe positive numbers entered are : {pos}")
print(f"\nThe negative numbers entered are : {neg}")

# Output
# Enter the N value = 5
# Enter the number 1 = 12
# Enter the number 2 = 23
# Enter the number 3 = -543
# Enter the number 4 = -23
# Enter the number 5 = 12
# The positive numbers entered are : [12, 23, 12]
# The negative numbers entered are : [-543, -23]