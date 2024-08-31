file=open("filename.txt","r")
total=0
count=0
while True:
    line=file.readline()
    if not line:
        break
    total+=int(line)
    count+=1
file.close()
if count>0:
    print(total/count)
else:
    print("\nNo numbers in file")