import random

EASY = 10
DIFFICULT = 5

def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high ")
        turns -= 1
        return turns
    elif user_guess < actual_answer:
        print("Too low")
        turns -= 1
        return turns
    else:
        print(f"You nailed it!")

def set_difficulty():
    user_level = input("choose difficulty 'easy' or 'hard': ")
    if user_level == 'easy':
        return EASY
    else:
        return DIFFICULT
    

com_number = random.randint(1, 100)
turns = set_difficulty()

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100")
print("You have 10 attempts remaining to guess the number")

print(f"You have {turns} attempts remaining to guess the number")

user_guess = 0
print(com_number)

while not (com_number == user_guess or turns == 0):
    user_guess = int(input("guess the number: "))
    if com_number != user_guess:
        check_answer(user_guess, com_number, turns)
        print(f"you have {turns} attemps remaining to guess the number")

