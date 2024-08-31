s=input("\nEnter the string = ")
numRows=int(input("\nEnter the number of rows = "))
if numRows==1:
    print(s)
else:
    rows=['']*min(numRows,len(s))
    curRow=0
    goingDown=False
    for char in s:
        rows[curRow]+=char
        if curRow==0 or curRow==numRows-1:
            goingDown=not goingDown
        curRow+=1 if goingDown else -1
    result=''.join(rows)
    print(result)

# Output
# Enter the string = PAYPALISHIRING
# Enter the number of rows = 3
# PAHNAPLSIIGYIR