#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
names = open("Mail Merge Project Start/Input/Names/invited_names.txt", mode ="r")

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt", mode ="r") as file:
    letter_contents = file.read()
    for name in names.readlines():
        inviting_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, inviting_name)
        with open(f"Mail Merge Project Start/ReadyToSend/invited_{inviting_name}.txt", mode='w') as letter:
            letter.write(new_letter)

        


        