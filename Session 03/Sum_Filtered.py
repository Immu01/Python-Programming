n=int(input("\nEnter the n value = "))
positive=[]
a=[]
for i in range(n):
    num = int(input(f"\nEnter the number {i+1} = "))
    if num>0:
        positive.append(num)
print(f"\nThe numbers = {positive}")
a=[num for num in positive if num<100]
print(f"\nThe number smaller than 100 are = {a}")
sum=sum(a)
print(f"\nThe sum of positive numbers which are less than 100 = {sum}")

# Output
# Enter the n value = 5
# Enter the number 1 = 12
# Enter the number 2 = 23
# Enter the number 3 = 458
# Enter the number 4 = -3568
# Enter the number 5 = 457
# The numbers = [12, 23, 458, 457]
# The number smaller than 100 are = [12, 23]
# The sum of positive numbers which are less than 100 = 35