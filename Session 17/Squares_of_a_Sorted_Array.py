nums=list(map(int,input("\nEnter the sorted array separated by spaces = ").split()))
squares=[x*x for x in nums]
squares.sort()
print(f"\nThe sorted squares are = {squares}")

# Output
# Enter the sorted array separated by spaces = -4 -1 0 3 10
# The sorted squares are = [0, 1, 9, 16, 100]