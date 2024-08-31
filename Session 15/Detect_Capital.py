word=input("\nEnter a word = ")
if word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower()):
    print("true")
else:
    print("false")

# Output
# Enter a word = USA
# true