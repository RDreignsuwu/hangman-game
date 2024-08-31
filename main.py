import random as rd
import hangmanwords as hwords
import hangman_draw as hd
word=rd.choice(hwords.word_list)
print(hd.logo)
wordlen=len(word)
blanks=["_"]*wordlen
lives=6
guessed_letters=[]
while blanks.count("_")!=0 and lives!=0:
    guess=input("Guess a letter\n").lower()
    if guess in guessed_letters:
        print("You have already guessed this\n")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(wordlen):
            if word[i]==guess:
                blanks[i]=guess
        print(''.join(blanks))
    elif guess not in word:
        print("You guessed incorrect!\n")
        lives-=1
        print(hd.stages[lives])

print("Game Over")
if lives==0:
    print(f"You lost!\nThe word was {word}")
else:
    print("You Won")
