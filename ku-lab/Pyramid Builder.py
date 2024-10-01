vowel = "aeiou"
word = str(input())
i = 0

for ch in word :
    if i < len(word) :
        if ch in vowel and ch != " ":
            print(word[i], end="")
            i+=3
        else:
            print(word[i], end="")
            i+=1