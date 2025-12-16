# first_string = input("Where have you born in?")
# second_string = input("What is your pet name?")
# band_name = first_string+" "+second_string
# print("your band name is "+band_name)
#
# print(len(band_name))

import random

# 1. randoly choose a word from the word list and assign it

d_list = ["aardvark", "baboon", "camel"]

the_word = random.randint(0,2)
print(the_word)
# ask the user to guess a letter and assign their 

# check if the letter the user guessed is Correct 


# ran_num = random.randint(1, 10)
# print(ran_num)
#
# random_number_0to1 = random.random() * 10 # 0~1 사이의 숫자생성
# print(random_number_0to1)

head_or_tail = random.randint(0, 1)

if head_or_tail == 0 :
    print("Head", head_or_tail)
else:
    print("Tail", head_or_tail)

number = random.randint(0, 6)

friends = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred"]
print(friends[number])
print(random.choice(friends))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

number_password = int(input("How many letters would you like in your password: "))
number_symbol = int(input("How many symbols would you like in your password: "))
number_number = int(input("How many numbers would you like in your password: "))

passwordList = []
if number_password > number_symbol + number_number:
    for i in range(0, number_symbol):
        passwordList.append(random.choice(symbols))
    for j in range(0, number_number):
        passwordList.append(random.choice(numbers))
    for k in range(0, number_password - number_symbol- number_number):
        passwordList.append(random.choice(letters))

print(passwordList)

random.shuffle(passwordList)

password = ''.join(passwordList)
print(f"Your generated password is: {password}")



