nums=list(map(int,input("\nEnter a list of integers (comma-separated) = ").split(',')))
result=["over" if num>100 else num for num in nums]
print(result)

# Output
# Enter a list of integers (comma-separated) = 10,120,50,200,85
# [10, 'over', 50, 'over', 85]