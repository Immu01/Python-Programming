def most_frequent(s):
    s=s.lower() 
    frequency={} 
    for letter in s:
        if letter.isalpha(): 
            if letter in frequency:
                frequency[letter]+=1 
            else:
                frequency[letter]=1
    for letter in sorted(frequency,key=frequency.get,reverse=True):
        print(letter,frequency[letter])
most_frequent("Hello World")

# Output
# l 3
# o 2
# h 1
# e 1
# w 1
# r 1
# d 1