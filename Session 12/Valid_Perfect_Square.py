num=int(input("\nEnter a number = "))
i=1
while i*i<=num:
    if i*i==num:
        print(f"\n{num} is a perfect square ")
        break
    i+=1
else:
    print(f"\n{num} is not a perfect square")

# Output
# Enter a number = 16
# 16 is a perfect square 