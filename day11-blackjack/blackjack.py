import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compare(user_score, com_score):
    if user_score == com_score:
        return "Draw"
    elif com_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with balckjack"
    elif user_score > 21:
        return "You went over, You lose"
    elif com_score > 21:
        return "Oppenent went over, You win"
    elif com_score < user_score:
        return "You win"
    else:
        return "You lose"

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

   
def play_game():
    dealer = []
    user = []
    com_score = -1
    user_score = -1
    is_gameover = False

    for _ in range(2):
        user.append(deal_card())
        dealer.append(deal_card())


    while not is_gameover: 
        user_score = calculate_score(user)
        com_score = calculate_score(dealer)
        print(f"Your cards: {user}, current_score: {user_score}")
        print(f"Dealer cards: {dealer[0]}")


        if user_score == 0 or com_score == 0 or user_score > 21:
            is_gameover = True
        else:
            user_should_deal = input("Type 'y' to get anotehr card, type 'n to pass: ")
            if user_should_deal == 'y':
                user.append(deal_card())
            else:
                is_gameover = True

    while com_score != 0 and com_score < 17 :
        dealer.append(deal_card())
        com_score = calculate_score(dealer)

    print(f"Your final cards: {user}, final score: {user_score}")
    print(compare(user_score, com_score))

while input("Do you want to play a Blackjack?  type 'y' or 'n': ") == 'y':
    print("\n")
    play_game()