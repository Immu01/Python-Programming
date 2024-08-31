s=input("\nEnter the string = ")
words=s.split()
reversed_words=words[::-1]
result=' '.join(reversed_words)
print(f"\nOutput = {result}")

# Output
# Enter the string = the sky is blue
# Output = blue is sky the