filename = input("\nEnter the filename = ")
try:
    with open(filename,'r') as file:
        print(file.read())
except FileNotFoundError:
    print("\nError : File not found")

# Output
# Enter the filename = Note 11
# Error : File not found