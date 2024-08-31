from collections import Counter
nums=list(map(int,input("\nEnter list of integers (comma-separated) = ").split(',')))
freq=Counter(nums)
for num in sorted(freq):
    print(f"{num} : {'*'*freq[num]}")

#   Output
# Enter list of integers (comma-separated) = 1,2,2,3,3,3
# 1 : *
# 2 : **
# 3 : ***