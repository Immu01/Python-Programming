file_name=input("\nEnter the file name = ")
file=open(file_name,"r")
while True:
    line=file.readline()
    if not line:
        break
    if '#' in line:
        print(line,end='')
file.close()