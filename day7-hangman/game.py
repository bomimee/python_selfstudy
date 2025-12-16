import random
# 1. randoly choose a word from the word list and assign it

d_list = ["aardvark", "baboon", "camel"]
life = 6

# ask the user to guess a letter and assign their 

game_over = False 
correct_letters = []
# check if the letter the user guessed is Correct 

the_word = random.choice(d_list)

placeholder = ''
word_length = len(the_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

while not game_over: 
    guess = input("guess the word : ").lower()
    display = ''    

    for letter in the_word:
        if guess == letter:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        
        else:
            display += "_"

    print(display)

    if guess not in the_word:
        life -= 1
        print(life)
        if life == 0:
            game_over = True
            print("You lose")

    if '_' not in display:
        game_over = True
        print("You win")
