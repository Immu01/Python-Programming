def is_anagram(word1,word2):
    return sorted(word1.lower())==sorted(word2.lower())
print(is_anagram("listen","silent"))
print(is_anagram("hello","world"))

# Output
# True
# False