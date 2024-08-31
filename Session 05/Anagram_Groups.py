def find_anagrams(word_list):
    anagram_dict={}
    for word in word_list:
        key=''.join(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key]=[word]
    for words in anagram_dict.values():
        if len(words)>1:
            print(words)
word_list=input("\nEnter words separated by spaces = ").split()
find_anagrams(word_list)

# Output
# Enter words separated by spaces = listen silent enlist tinsel inlets
# ['listen', 'silent', 'enlist', 'tinsel', 'inlets']