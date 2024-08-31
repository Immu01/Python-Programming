names=[]
while True:
    name=input("\nEnter a first name (or press Enter to finish) = ")
    if name=="":
        break
    names.append(name)
count=0
for name in names:
    for char in name:
        if char.lower()=='a':
            count+=1
print(f"\nThe letter 'a' appears {count} times")

# Output
# Enter a first name (or press Enter to finish) = Elephant
# Enter a first name (or press Enter to finish) = Malayalam
# Enter a first name (or press Enter to finish) = African
# Enter a first name (or press Enter to finish) = 
# The letter 'a' appears 7 times