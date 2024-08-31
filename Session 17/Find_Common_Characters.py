words=input("\nEnter the list of words separated by commas = ").split(',')
words=[word.strip() for word in words]
result=[]
for char in set(words[0]):
    min_count=min(word.count(char) for word in words)
    result.extend([char]*min_count)
print(f"\nCommon characters are = {result}")

# Output
# Enter the list of words separated by commas = cook lock cook
# Common characters are = [' ', ' ', 'k', 'k', 'k', 'l', 'o', 'o', 'o', 'o', 'o', 'c', 'c', 'c']