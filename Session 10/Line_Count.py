file=open(".txt","r")
count=0
while True:
    line=file.readline()
    if not line:
        break
    count+=1
file.close()
print(f"\nNumber of lines = {count}")