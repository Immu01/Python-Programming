file=open("filename.txt","r")
while True:
    line=file.readline()
    if not line:
        break
    line=line.lower()
    word=""
    for char in line:
        if char.isalpha() or char.isspace():
            if char!=' ':
                word+=char
        elif char==' ':
            if word:
                print(word)
                word=""
    if word:
        print(word)
file.close()