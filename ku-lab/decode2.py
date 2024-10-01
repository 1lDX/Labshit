vowel = "aeiou"
word = str(input())
i = 0

for ch in word :
    if word[i] in vowel and word[i] != " ":
        print(word[i], end="")
        i+=3
    elif i < len(word) :
        print(word[i], end="")
        i+=1

       
    
    