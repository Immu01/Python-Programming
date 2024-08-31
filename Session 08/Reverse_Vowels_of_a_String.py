s=input("\nEnter a string = ")
vowels="aeiouAEIOU"
s_list=list(s)
i,j=0,len(s_list)-1
while i<j:
    if s_list[i] in vowels and s_list[j] in vowels:
        s_list[i],s_list[j]=s_list[j],s_list[i]
        i+=1
        j-=1
    if s_list[i] not in vowels:
        i+=1
    if s_list[j] not in vowels:
        j-=1
print(''.join(s_list))

# Output
# Enter a string = hello
# holle