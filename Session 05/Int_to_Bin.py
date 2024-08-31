n=42
s=""
while n>0:
    s=str(n%2)+s
    n=n//2
if s=="":
    s="0"
print("\nBinary representation = ",s)

# Output
# Binary representation =  101010