def bid_program():
    should_continue = True
    bid_dict = {}
    while should_continue:
        user_continue = input('you want to continue?: ')
        if user_continue == 'y':
            your_name = input("what is your name: ")
            your_bid = int(input("what's your bid: "))
            bid_dict[your_name] = your_bid
        else:
            should_continue = False
    highest_price = 0
    the_name = ''
    for key in bid_dict:
        if bid_dict[key] > highest_price:
            highest_price = bid_dict[key] 
            the_name = key 
        print("key", key)
        print("NAME", the_name)
    print(f"the winner is {the_name} with {highest_price}")


bid_program() 