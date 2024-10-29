import random

words = ['python', 'sql', 'html', 'css', 'java', 'javascript', 'ruby', 'swift']

chosen_words = random.choice(words)
word_display = ['_' for i in chosen_words] #To loop the '_' in the same line. 
print(chosen_words)
print(word_display)
attempts = 8

print("Welcome to Hangman!!!!!")

while attempts > 0 and '_' in word_display:
    print( "\n" + ' '.join(word_display)) # give space to the each '_' after this.
    guess =  input("Guess the letter: ").lower()
    if guess in chosen_words:
        for index, letter in enumerate(chosen_words): #enumarate is used automatically goes into the fixed field.
            print(letter,"aaaaaaaaaa")
            print(index,"bbbbbbbbb")
            if letter == guess:
                word_display[index] = guess
    else:
        print("The letter doesn't appear in that word!!!!.")   
        attempts -= 1         


if '_' not in word_display:
    print("You guessed the word correctly!!!!!!.")
    print(' '.join(word_display))
    print("You Survived")
else:
    print("You ran out of attempts. The word is : " + chosen_words)    
    print("You lost")
