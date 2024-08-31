n=int(input("\nEnter number of rows = "))
triangle=[]
for i in range(n):
    row=[1]*(i+1)
    for j in range(1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
    triangle.append(row)
max_width=len(' '.join(map(str,triangle[-1])))
for row in triangle:
    print(' '.join(map(str,row)).center(max_width))

# Output
# Enter number of rows = 5
#     1    
#    1 1   
#   1 2 1  
#  1 3 3 1 
# 1 4 6 4 1