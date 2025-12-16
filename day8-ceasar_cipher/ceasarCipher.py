should_continue = True

while should_continue:
    want_continue = input("you want to continue?: ").lower()
    if want_continue == 'y':
        type = input("type 'encode' for encoding, type 'decode' for decoding: ")
        userString = input("give the setence or word: ").lower()
        number = int(input("give the number: "))


        def encodeDecode(type, userString, number):
            newString = ''
            new_number = number if type == "encode" else -number
            for char in userString:
                base = ord('a')
                newChar = chr((ord(char) - base + new_number) % 26 + base)
                newString += newChar
            print(newString)

        encodeDecode(type, userString, number)
    else:
        should_continue = False

