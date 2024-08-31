def areTriangular(a,b,c):
    return a+b>c and a+c>b and b+c>a
print(areTriangular(3,4,5))
print(areTriangular(1,2,3))

# Output
# True
# False