x=int(input("\nEnter an integer = "))
original=x
reversed_num=0
while x>0:
    digit=x%10
    reversed_num=reversed_num*10+digit
    x//=10
print(original==reversed_num)

# Output
# Enter an integer = 121
# True