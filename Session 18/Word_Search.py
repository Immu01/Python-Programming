m=int(input("\nEnter the number of rows in the grid = "))
n=int(input("\nEnter the number of columns in the grid = "))
board=[]
for i in range(m):
    row=input(f"\nEnter row {i + 1} elements separated by spaces = ").split()
    board.append(row)
word=input("\nEnter the word to search for = ")
found=False
def dfs(x,y,index):
    if index==len(word):
        return True
    if x<0 or x>=m or y<0 or y>=n or board[x][y]!=word[index]:
        return False
    temp=board[x][y]
    board[x][y]='#'
    result=(dfs(x+1,y,index+1) or
              dfs(x-1,y,index+1) or
              dfs(x,y+1,index+1) or
              dfs(x,y-1,index+1))
    board[x][y]=temp
    return result
for i in range(m):
    for j in range(n):
        if dfs(i,j,0):
            found=True
            break
    if found:
        break
print(f"\nOutput = {found} ")

# Output
# Enter the number of rows in the grid = 3
# Enter the number of columns in the grid = 4
# Enter row 1 elements separated by spaces = A B C E
# Enter row 2 elements separated by spaces = S F C S
# Enter row 3 elements separated by spaces = A D E E
# Enter the word to search for = ABCCED
# Output = True 