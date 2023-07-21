#importing of functions:
import os
import random
from hangman_word_list import word_list
from hangman_art import stages,logo

#printing the logo:
print(logo)
#Random word generation:
chosen_word=random.choice(word_list)
#testing code:
#print(f"the chosen word is {chosen_word}")
#displaying the dashes in the place of word
display=[]
dash=len(chosen_word)
for d in range(0,dash):
    display.append("_")
print(display)
#using a while loop to give the player chances to guess until all the blanks are replaced with letters:
end_of_game=False
lives=6
while not end_of_game :
#asking for the users guess:
    guess=input("Guess a letter in the word: ").lower()
#for clearing the screen up after the result of every guess in printed:    
    os.system("clear")
    
    if guess in display:
        print("Letter has been already guessed!")
#checking and showing if the word exists in the guess:
    for i in range(len(chosen_word)):
        if chosen_word[i]==guess:
            display[i]=guess       
    print(display)
    if guess not in chosen_word:
        print(f"your guess {guess} is not in the word !! You lose a life !")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose!!!")   
    elif "_" not in display:
        end_of_game=True
        print("You win!")
    print(stages[lives])
