rows=int(input("\nEnter the number of rows in the triangle = "))
triangle=[]
for i in range(rows):
    row=list(map(int,input(f"\nEnter row {i + 1} elements separated by spaces = ").split()))
    triangle.append(row)
for i in range(rows-2,-1,-1):
    for j in range(len(triangle[i])):
        triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
print("\nOutput = ",triangle[0][0])

# Output
# Enter the number of rows in the triangle = 4 
# Enter row 1 elements separated by spaces = 2
# Enter row 2 elements separated by spaces = 3 4
# Enter row 3 elements separated by spaces = 6 5 7
# Enter row 4 elements separated by spaces = 4 1 8 3
# Output =  11