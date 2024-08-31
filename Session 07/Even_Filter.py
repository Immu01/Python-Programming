def evenFilter(d):
    return [v for k,v in d.items() if k%2==0]
n=int(input("\nEnter number of elements = "))
d={}
for _ in range(n):
    key,value=map(int,input("\nEnter key and value (separated by space) = ").split())
    d[key]=value
print(evenFilter(d))

# Output
# Enter number of elements = 4
# Enter key and value (separated by space) = 1 10
# Enter key and value (separated by space) = 2 20
# Enter key and value (separated by space) = 3 30
# Enter key and value (separated by space) = 4 40
# [20, 40]