
import random
joon=6
words_bank =["book","moon","tree","sadjad","university","python","c++","apple","corona"]
word=random.choice(words_bank)
user_word=len(word)*'-'
user_correct_char=[]

while joon>0 and word!=user_word:
    print(user_word)
    character=input("plrase enter the character : ")
    character=character.lower()
    if character in word :
        for i in range(len(word)):
            if character==word[i]:
                temp=list(user_word)
                temp[i]=character
                user_word="".join(temp)
    if character not in word:
        joon=joon-1
        print("❌")
    if word==user_word:
        print(user_word)
        print("you win")
    if joon==0:
        print("game over")
        