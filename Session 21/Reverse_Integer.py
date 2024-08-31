x=int(input("\nEnter an integer = "))
sign=-1 if x<0 else 1
x*=sign
reversed_num=0
while x!=0:
    reversed_num=reversed_num*10+x%10
    x//=10
reversed_num*=sign
if reversed_num<-2**31 or reversed_num>2**31-1:
    reversed_num=0
print(reversed_num)

# Output
# Enter an integer = 321
# 123